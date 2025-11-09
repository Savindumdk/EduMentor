import os
import re
import json
import warnings
import pdfplumber
import google.generativeai as genai
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Suppress pdfplumber warnings about PDF color values
warnings.filterwarnings('ignore', category=UserWarning, module='pdfminer')

# --- CONFIG ---
PDF_PATH = "science.pdf"
OUTPUT_DIR = "knowledge_base"
BIO_FILE   = os.path.join(OUTPUT_DIR, "biology_rules.py")
PHY_FILE   = os.path.join(OUTPUT_DIR, "physics_rules.py")
CHEM_FILE  = os.path.join(OUTPUT_DIR, "chemistry_rules.py")

# Set your Gemini API key from .env file
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file!\n"
        "Please add it to your .env file: GEMINI_API_KEY=your-api-key-here"
    )
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"  # or a suitable variant
CHUNK_SIZE = 2000  # number of characters per chunk

# --- FUNCTIONS ---
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF, suppressing warnings."""
    text = ""
    # Suppress warnings during PDF processing
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:  # Only add if text was extracted
                    text += page_text + "\n"
    return text

def chunk_text(text: str, size: int) -> List[str]:
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i+size])
    return chunks

def call_gemini(prompt: str) -> str:
    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)
    return response.text

def clean_concept_name(name: str) -> str:
    # simple sanitization for variable/method names
    return re.sub(r"\W|^(?=\d)", "_", name).lower()

def build_rule(concept: str, explanation: str, topic: str, subtopic: str, examples: List[str]) -> str:
    name = clean_concept_name(concept)
    rule = f"""    @Rule(Fact(query_topic='{name}'))
    def rule_{name}(self):
        \"\"\"{explanation.splitlines()[0]}\"\"\"
        self.response = {{
            'concept': '{concept}',
            'explanation': \"\"\"{explanation}\"\"\",
            'topic': '{topic}',
            'subtopic': '{subtopic}',
            'examples': {json.dumps(examples, ensure_ascii=False)}
        }}
        self.halt()
"""
    return rule

def process_chunk(chunk: str) -> List[Dict]:
    """Process a text chunk and extract educational rules using Gemini."""
    prompt = f"""You are an educational rule generator. Given the following textbook excerpt, generate structured rules in JSON format.  
Return a JSON array (list) of objects with these exact keys: concept, explanation, topic, subtopic, examples.  
The 'examples' field should be an array of 2-3 example strings.

Excerpt:
\"\"\"{chunk}\"\"\"  

Make sure each object is for one concept. Return ONLY valid JSON, no markdown or extra text.
Example format:
[
  {{
    "concept": "Concept Name",
    "explanation": "Detailed explanation here",
    "topic": "Biology/Physics/Chemistry",
    "subtopic": "Subtopic name",
    "examples": ["Example 1", "Example 2"]
  }}
]"""
    
    try:
        resp = call_gemini(prompt)
        # Try to extract JSON from response (in case it has markdown wrapper)
        resp = resp.strip()
        if resp.startswith("```json"):
            resp = resp[7:]
        if resp.startswith("```"):
            resp = resp[3:]
        if resp.endswith("```"):
            resp = resp[:-3]
        resp = resp.strip()
        
        rules = json.loads(resp)
        if not isinstance(rules, list):
            print("WARNING: Response is not a list, wrapping it")
            rules = [rules] if isinstance(rules, dict) else []
        return rules
    except json.JSONDecodeError as e:
        print(f"WARNING: Could not parse JSON: {e}")
        print(f"Response was: {resp[:200]}...")
        return []
    except Exception as e:
        print(f"ERROR processing chunk: {e}")
        return []

def write_rules_to_file(rules: List[Dict], filepath: str):
    with open(filepath, "a", encoding="utf-8") as f:
        for r in rules:
            rule_text = build_rule(r['concept'], r['explanation'], r['topic'], r['subtopic'], r['examples'])
            f.write(rule_text + "\n")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    text = extract_text_from_pdf(PDF_PATH)
    chunks = chunk_text(text, CHUNK_SIZE)
    for chunk in chunks:
        rules = process_chunk(chunk)
        for r in rules:
            topic = r.get('topic', '').lower()
            if "biology" in topic:
                write_rules_to_file([r], BIO_FILE)
            elif "physics" in topic:
                write_rules_to_file([r], PHY_FILE)
            elif "chemistry" in topic:
                write_rules_to_file([r], CHEM_FILE)
            else:
                # default: chemistry
                write_rules_to_file([r], CHEM_FILE)
    print("Done: rules generation completed.")

if __name__ == "__main__":
    main()
