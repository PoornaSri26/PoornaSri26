#!/usr/bin/env python3
"""
Error checking script for GitHub profile
"""

import requests
import os
import re

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'PoornaSri26')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')

def check_repository_links():
    """Check if all repository links in README are valid"""
    print("Checking repository links...")
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Extract all GitHub repository links
    repo_links = re.findall(r'https://github.com/[^\s\)]+', readme_content)
    
    broken_links = []
    for link in repo_links:
        try:
            response = requests.head(link, timeout=5)
            if response.status_code >= 400:
                broken_links.append(link)
                print(f"Broken link: {link} (Status: {response.status_code})")
        except Exception as e:
            broken_links.append(link)
            print(f"Error checking {link}: {e}")
    
    if not broken_links:
        print("All repository links are valid!")
    else:
        print(f"Found {len(broken_links)} broken links")
    
    return len(broken_links) == 0

def check_image_links():
    """Check if all image links are valid"""
    print("Checking image links...")
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Extract all image URLs (including SVG files)
    image_links = re.findall(r'https://[^\s\)]+\.(?:png|jpg|jpeg|gif|svg)', readme_content)
    
    # Also check local assets
    local_images = re.findall(r'assets/[^\s\)]+\.(?:png|jpg|jpeg|gif|svg)', readme_content)
    
    broken_images = []
    
    # Check external URLs
    for link in image_links:
        try:
            response = requests.head(link, timeout=5)
            if response.status_code >= 400:
                broken_images.append(link)
                print(f"Broken image: {link} (Status: {response.status_code})")
        except Exception as e:
            # Some external services might not allow HEAD requests
            try:
                response = requests.get(link, timeout=5, stream=True)
                if response.status_code >= 400:
                    broken_images.append(link)
                    print(f"Broken image: {link} (Status: {response.status_code})")
            except Exception as e2:
                broken_images.append(link)
                print(f"Error checking {link}: {e2}")
    
    # Check local files
    for local_img in local_images:
        if not os.path.exists(local_img):
            broken_images.append(local_img)
            print(f"Missing local image: {local_img}")
    
    if not broken_images:
        print("All image links are valid!")
    else:
        print(f"Found {len(broken_images)} broken image links")
    
    return len(broken_images) == 0

def check_markdown_syntax():
    """Check for common markdown syntax errors"""
    print("Checking markdown syntax...")
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    errors = []
    
    # Check for unclosed code blocks
    code_blocks = re.findall(r'```', readme_content)
    if len(code_blocks) % 2 != 0:
        errors.append("Unclosed code blocks detected")
    
    # Check for unclosed links
    unclosed_links = re.findall(r'\[([^\]]+)$', readme_content, re.MULTILINE)
    if unclosed_links:
        errors.append(f"Unclosed links: {unclosed_links}")
    
    # Check for table formatting
    tables = re.findall(r'\|.*?\|', readme_content, re.MULTILINE)
    for table in tables:
        if not table.startswith('|') or not table.endswith('|'):
            errors.append(f"Malformed table row: {table}")
    
    if not errors:
        print("Markdown syntax looks good!")
    else:
        print(f"Found {len(errors)} markdown errors:")
        for error in errors:
            print(f"  - {error}")
    
    return len(errors) == 0

def check_repo_existence():
    """Check if referenced repositories actually exist"""
    print("Checking repository existence...")
    
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Extract repository names from links
    repo_names = re.findall(r'github.com/' + GITHUB_USERNAME + r'/([^\s\)]+)', readme_content)
    
    missing_repos = []
    for repo_name in repo_names:
        url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 404:
                missing_repos.append(repo_name)
                print(f"Missing repository: {repo_name}")
        except Exception as e:
            print(f"Error checking {repo_name}: {e}")
    
    if not missing_repos:
        print("All referenced repositories exist!")
    else:
        print(f"Found {len(missing_repos)} missing repositories")
    
    return len(missing_repos) == 0

def generate_error_report():
    """Generate comprehensive error report"""
    print("=" * 50)
    print("GITHUB PROFILE ERROR CHECK REPORT")
    print("=" * 50)
    
    results = {
        'Repository Links': check_repository_links(),
        'Image Links': check_image_links(),
        'Markdown Syntax': check_markdown_syntax(),
        'Repository Existence': check_repo_existence()
    }
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    all_passed = True
    for check, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        print(f"{check}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("All checks passed! Profile is healthy.")
    else:
        print("Some checks failed. Please review the errors above.")
    
    return all_passed

if __name__ == '__main__':
    generate_error_report()