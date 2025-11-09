"""
Quick Start Script for EduMentor Phase 2+3
-------------------------------------------
Quickly run or test the EduMentor system.
"""

import sys
import subprocess
import os


def print_menu():
    """Display the main menu."""
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           EduMentor Phase 2+3 Quick Start               ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Please choose an option:

1. 🚀 Run EduMentor (Streamlit UI)
2. 🧪 Run Tests
3. 🔧 Setup/Install Dependencies
4. 📊 Check System Status
5. 📖 View Documentation
6. ❌ Exit

""")


def run_application():
    """Run the Streamlit application."""
    print("\n🚀 Starting EduMentor...\n")
    print("The application will open in your browser.")
    print("Press Ctrl+C to stop the server.\n")
    
    try:
        subprocess.run(["streamlit", "run", "main.py"])
    except KeyboardInterrupt:
        print("\n\n✓ Application stopped.")
    except FileNotFoundError:
        print("❌ Error: Streamlit not found. Please run setup first (option 3).")


def run_tests():
    """Run the test suite."""
    print("\n🧪 Running tests...\n")
    
    try:
        subprocess.run([sys.executable, "test_system.py"])
    except Exception as e:
        print(f"❌ Error running tests: {e}")


def run_setup():
    """Run the setup script."""
    print("\n🔧 Running setup...\n")
    
    try:
        subprocess.run([sys.executable, "setup.py"])
    except Exception as e:
        print(f"❌ Error running setup: {e}")


def check_status():
    """Check system status."""
    print("\n📊 Checking system status...\n")
    
    # Check Python version
    print(f"✓ Python: {sys.version.split()[0]}")
    
    # Check required packages
    packages = [
        'experta',
        'streamlit',
        'google.generativeai',
        'frozendict'
    ]
    
    print("\nInstalled Packages:")
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg}")
        except ImportError:
            print(f"  ✗ {pkg} (NOT INSTALLED)")
    
    # Check environment
    print("\nEnvironment Configuration:")
    if os.path.exists('.env'):
        print("  ✓ .env file exists")
        
        # Check if API key is set
        with open('.env', 'r') as f:
            content = f.read()
            if 'GEMINI_API_KEY' in content and 'your_gemini_api_key_here' not in content:
                print("  ✓ GEMINI_API_KEY configured")
            else:
                print("  ⚠️ GEMINI_API_KEY not configured (LLM features disabled)")
    else:
        print("  ✗ .env file not found")
    
    # Check file structure
    print("\nProject Structure:")
    required_dirs = ['agents', 'subjects', 'llm', 'utils']
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"  ✓ {dir_name}/")
        else:
            print(f"  ✗ {dir_name}/ (MISSING)")
    
    print("\n" + "="*60 + "\n")


def view_docs():
    """Display documentation menu."""
    print("""
📖 Documentation Files:

1. README.md - Complete system overview
2. QUICK_REFERENCE.md - Quick reference guide
3. ARCHITECTURE.md - System architecture
4. config.py - Configuration settings

Choose a file number to view (or 0 to return): """, end='')
    
    choice = input().strip()
    
    docs = {
        '1': 'README.md',
        '2': 'QUICK_REFERENCE.md',
        '3': 'ARCHITECTURE.md',
        '4': 'config.py'
    }
    
    if choice in docs:
        filename = docs[choice]
        if os.path.exists(filename):
            print(f"\n📄 {filename}:\n")
            with open(filename, 'r', encoding='utf-8') as f:
                print(f.read())
            print("\n" + "="*60)
            input("\nPress Enter to continue...")
        else:
            print(f"❌ File not found: {filename}")
    elif choice != '0':
        print("❌ Invalid choice")


def main():
    """Main menu loop."""
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            run_application()
        elif choice == '2':
            run_tests()
        elif choice == '3':
            run_setup()
        elif choice == '4':
            check_status()
        elif choice == '5':
            view_docs()
        elif choice == '6':
            print("\n👋 Goodbye! Happy learning!\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 6.\n")
        
        if choice != '1':  # Don't wait after running app (it blocks)
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
