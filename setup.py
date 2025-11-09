"""
Setup Script for EduMentor Phase 2+3
-------------------------------------
Installs dependencies and sets up the environment.
"""

import subprocess
import sys
import os


def print_header(text):
    """Print formatted header."""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def check_python_version():
    """Check if Python version is compatible."""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Error: Python 3.8 or higher is required")
        sys.exit(1)
    
    print("✓ Python version is compatible")


def install_dependencies():
    """Install required packages."""
    print_header("Installing Dependencies")
    
    print("Installing packages from requirements.txt...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("\n✓ All dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing dependencies: {e}")
        sys.exit(1)


def setup_environment():
    """Set up environment file."""
    print_header("Setting Up Environment")
    
    if os.path.exists('.env'):
        print("✓ .env file already exists")
        return
    
    if os.path.exists('.env.example'):
        print("Creating .env file from .env.example...")
        with open('.env.example', 'r') as src:
            with open('.env', 'w') as dst:
                dst.write(src.read())
        print("✓ .env file created")
        print("\n⚠️ IMPORTANT: Edit .env file and add your GEMINI_API_KEY")
    else:
        print("⚠️ Warning: .env.example not found")


def verify_installation():
    """Verify that key packages are installed."""
    print_header("Verifying Installation")
    
    packages = [
        ('experta', 'Experta (Expert System)'),
        ('streamlit', 'Streamlit (UI Framework)'),
        ('google.generativeai', 'Google Gemini (LLM)')
    ]
    
    all_ok = True
    for package, name in packages:
        try:
            __import__(package)
            print(f"✓ {name} installed")
        except ImportError:
            print(f"❌ {name} NOT installed")
            all_ok = False
    
    if all_ok:
        print("\n✓ All packages verified successfully")
    else:
        print("\n❌ Some packages are missing. Run setup again.")
        sys.exit(1)


def display_next_steps():
    """Display next steps for the user."""
    print_header("Setup Complete!")
    
    print("""
Next steps:

1. Get your Gemini API key:
   - Visit: https://makersuite.google.com/app/apikey
   - Create an API key
   - Copy the key

2. Configure your .env file:
   - Open .env in a text editor
   - Replace 'your_gemini_api_key_here' with your actual API key
   - Save the file

3. Run the application:
   - Execute: streamlit run main_v2.py
   - Open your browser to the URL shown

4. Start learning!
   - Ask questions in English, Sinhala, or Tamil
   - Toggle AI enhancement on/off
   - Explore all 6 subjects

For more information, see:
- README.md: General overview
- QUICKSTART.md: Quick start guide
- ARCHITECTURE.md: System architecture

Happy learning! 🎓
""")


def main():
    """Main setup function."""
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         EduMentor Phase 2+3 Setup Script                ║
║         Multi-Agent System + LLM Integration            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
""")
    
    try:
        check_python_version()
        install_dependencies()
        setup_environment()
        verify_installation()
        display_next_steps()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
