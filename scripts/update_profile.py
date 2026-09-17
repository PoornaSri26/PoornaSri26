#!/usr/bin/env python3
"""
Auto-update GitHub profile with new repositories
"""

import requests
import os
from datetime import datetime

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'PoornaSri26')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')

def get_user_repositories():
    """Fetch all repositories for the user"""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    params = {'sort': 'updated', 'per_page': 100}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_repo_description(repo):
    """Get detailed description for a repository"""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo['name']}/readme"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            readme_data = response.json()
            import base64
            import re
            content = base64.b64decode(readme_data['content']).decode('utf-8')
            # Extract first paragraph for description
            match = re.search(r'^#+ .*?\n\n(.*?)(?:\n\n|$)', content, re.MULTILINE)
            if match:
                return match.group(1)[:200] + "..."
    except:
        pass
    
    return repo.get('description', 'No description available')

def get_repo_languages(repo):
    """Get languages used in repository"""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo['name']}/languages"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            languages = response.json()
            return ', '.join(list(languages.keys())[:3])
    except:
        pass
    
    return 'Unknown'

def get_repo_topics(repo):
    """Get topics/tags for repository"""
    headers = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo['name']}/topics"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            topics = response.json().get('names', [])
            return topics[0] if topics else 'General'
    except:
        pass
    
    return 'General'

def categorize_repo(repo):
    """Categorize repository based on name and topics"""
    name = repo['name'].lower()
    topics = get_repo_topics(repo).lower()
    
    categories = {
        'AI Research': ['ai', 'ml', 'machine', 'learning', 'neural', 'deep', 'cognitive', 'eeg', 'fusion'],
        'Gaming': ['game', 'geo', 'shape', 'multiplayer', 'guess'],
        'Education': ['sort', 'algorithm', 'visualizer', 'learn', 'tutorial'],
        'Networking': ['network', 'router', 'lab', 'adaptive'],
        'ML': ['spam', 'detector', 'classification', 'email'],
        'Blockchain': ['blockchain', 'voting', 'smart', 'contract', 'web3'],
        'NLP': ['spell', 'telugu', 'language', 'nlp', 'search'],
        'Featured': ['solo', 'quest', 'productivity', 'rpg']
    }
    
    for category, keywords in categories.items():
        if any(keyword in name or keyword in topics for keyword in keywords):
            return category
    
    return 'General'

def generate_project_table(repos):
    """Generate markdown table for projects"""
    table = "| Project / Codebase | Technical Narrative & Observations | Core Stack | Status |\n"
    table += "| :--- | :--- | :--- | :--- |\n"
    
    for repo in repos[:12]:  # Top 12 repositories
        name = repo['name']
        description = get_repo_description(repo)
        languages = get_repo_languages(repo)
        category = categorize_repo(repo)
        
        table += f"| **[{name}](https://github.com/{GITHUB_USERNAME}/{name})** <br> <sub>[{category}]</sub> | **{description}**<br>• Latest updates and active development<br>• Community-driven improvements<br>• Open source contributions welcome | {languages} | `Active` |\n"
    
    return table

def update_readme():
    """Update README.md with new repository information"""
    repos = get_user_repositories()
    
    # Filter out forks and archived repos
    active_repos = [repo for repo in repos if not repo['fork'] and not repo['archived']]
    
    # Generate project table
    project_table = generate_project_table(active_repos)
    
    # Read current README
    with open('README.md', 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Replace the project table section
    import re
    pattern = r'\|\| Project / Codebase \| Technical Narrative & Observations \| Core Stack \| Status \|\|.*?\|\| :--- \|\| :--- \|\| :--- \|\|.*?(?=\n---)'
    replacement = project_table + '\n---'
    
    updated_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    # Update stats
    repo_count = len(active_repos)
    stars = sum(repo['stargazers_count'] for repo in active_repos)
    
    stats_pattern = r'\*\*([0-9]+) Public Repositories\*\*'
    updated_content = re.sub(stats_pattern, f'**{repo_count} Public Repositories**', updated_content)
    
    stars_pattern = r'\*\*([0-9]+) Stars Earned\*\*'
    updated_content = re.sub(stars_pattern, f'**{stars} Stars Earned**', updated_content)
    
    # Write updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"Updated profile with {repo_count} repositories and {stars} stars")

if __name__ == '__main__':
    update_readme()