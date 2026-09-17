#!/usr/bin/env python3
"""
Setup script for GitHub profile automation
"""

import os
import subprocess
import sys

def install_dependencies():
    """Install required Python packages"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies")
        return False

def create_directories():
    """Create necessary directories"""
    print("Creating directories...")
    directories = ['assets', 'output']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

def test_banner_generation():
    """Test banner generation"""
    print("Testing banner generation...")
    try:
        subprocess.check_call([sys.executable, 'generate_banner.py'])
        print("Banner generation test passed!")
        return True
    except subprocess.CalledProcessError:
        print("Banner generation test failed")
        return False

def test_error_check():
    """Test error checking"""
    print("Testing error checking...")
    try:
        subprocess.check_call([sys.executable, 'error_check.py'])
        print("Error check test passed!")
        return True
    except subprocess.CalledProcessError:
        print("Error check test failed")
        return False

def main():
    """Main setup function"""
    print("=" * 50)
    print("GITHUB PROFILE AUTOMATION SETUP")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("Setup failed: Could not install dependencies")
        return False
    
    # Test components
    print("\nTesting components...")
    banner_ok = test_banner_generation()
    error_check_ok = test_error_check()
    
    if banner_ok and error_check_ok:
        print("\n" + "=" * 50)
        print("SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        print("\nNext steps:")
        print("1. Customize config.py with your information")
        print("2. Add GITHUB_TOKEN to repository secrets")
        print("3. Push changes to trigger the automation")
        print("4. Monitor the Actions tab for workflow runs")
        return True
    else:
        print("\nSetup completed with some issues. Please review the errors above.")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)