#!/usr/bin/env python3
"""
Test script to verify chatbot setup
Checks all dependencies, file structure, and API key configuration
"""

import os
import sys
from pathlib import Path

def check_mark(success, message):
    """Print check mark or X"""
    symbol = "✅" if success else "❌"
    print(f"{symbol} {message}")
    return success

def main():
    print("=" * 60)
    print("🧪 Chatbot Setup Verification")
    print("=" * 60)
    print()
    
    all_checks = []
    
    # Get base directory
    base_dir = Path(__file__).parent
    os.chdir(base_dir)
    
    # Check 1: Python version
    print("1️⃣ Python Environment")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        all_checks.append(check_mark(True, f"Python {version.major}.{version.minor}.{version.micro}"))
    else:
        all_checks.append(check_mark(False, f"Python {version.major}.{version.minor}.{version.micro} (need 3.8+)"))
    print()
    
    # Check 2: Required packages
    print("2️⃣ Python Dependencies")
    packages = {
        'flask': 'Flask',
        'flask_cors': 'Flask-CORS',
        'requests': 'Requests'
    }
    
    for module, name in packages.items():
        try:
            __import__(module)
            all_checks.append(check_mark(True, f"{name} installed"))
        except ImportError:
            all_checks.append(check_mark(False, f"{name} NOT installed"))
    print()
    
    # Check 3: File structure
    print("3️⃣ File Structure")
    files_to_check = {
        'chatbot.html': 'Main HTML interface',
        'scripts/server.py': 'Flask server script',
        'requirements.txt': 'Dependencies file',
        'README.md': 'Documentation'
    }
    
    for filepath, description in files_to_check.items():
        path = base_dir / filepath
        all_checks.append(check_mark(path.exists(), f"{description}: {filepath}"))
    print()
    
    # Check 4: Directories
    print("4️⃣ Directories")
    dirs_to_check = {
        'scripts': 'Scripts directory',
        'chatHistory': 'Chat history directory'
    }
    
    for dirpath, description in dirs_to_check.items():
        path = base_dir / dirpath
        exists = path.exists() and path.is_dir()
        all_checks.append(check_mark(exists, f"{description}: {dirpath}/"))
        if not exists and dirpath == 'chatHistory':
            print(f"   ℹ️  Will be created automatically by server")
    print()
    
    # Check 5: API key
    print("5️⃣ API Configuration")
    api_key_file = base_dir.parent / "Data" / "GenAIkey.md"
    if api_key_file.exists():
        try:
            with open(api_key_file, 'r') as f:
                content = f.read().strip()
                # Remove markdown code blocks
                if content.startswith('```'):
                    lines = content.split('\n')
                    content = '\n'.join(lines[1:-1]).strip()
                if content:
                    all_checks.append(check_mark(True, f"API key file found: {api_key_file}"))
                    all_checks.append(check_mark(True, f"API key loaded (length: {len(content)} chars)"))
                else:
                    all_checks.append(check_mark(False, "API key file exists but is empty"))
        except Exception as e:
            all_checks.append(check_mark(False, f"Error reading API key: {e}"))
    else:
        all_checks.append(check_mark(False, f"API key file not found: {api_key_file}"))
    print()
    
    # Check 6: Server script syntax
    print("6️⃣ Server Script")
    server_script = base_dir / "scripts" / "server.py"
    if server_script.exists():
        try:
            with open(server_script, 'r') as f:
                code = f.read()
                compile(code, str(server_script), 'exec')
            all_checks.append(check_mark(True, "Server script syntax is valid"))
        except SyntaxError as e:
            all_checks.append(check_mark(False, f"Server script has syntax errors: {e}"))
    else:
        all_checks.append(check_mark(False, "Server script not found"))
    print()
    
    # Summary
    print("=" * 60)
    passed = sum(all_checks)
    total = len(all_checks)
    print(f"📊 Summary: {passed}/{total} checks passed")
    print("=" * 60)
    print()
    
    if passed == total:
        print("✅ All checks passed! Your chatbot is ready to use.")
        print()
        print("To start the server:")
        print("  python3 scripts/server.py")
        print()
        print("Or use the quick start script:")
        print("  ./start.sh")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
        print()
        print("Common fixes:")
        print("  • Install dependencies: pip install -r requirements.txt")
        print("  • Create missing directories")
        print("  • Verify API key file exists at: ../Data/GenAIkey.md")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())

