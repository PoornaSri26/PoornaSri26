#!/usr/bin/env python3
"""
Configuration for GitHub profile automation
"""

# User Information
USER_CONFIG = {
    'name': 'Poorna Sri',
    'username': 'PoornaSri26',
    'role': 'Full Stack Engineer / AI/ML Enthusiast / Tech Innovator',
    'location': 'Hyderabad, India',
    'email': 'poornasri26@gmail.com',
    'linkedin': 'https://linkedin.com/in/poornasri26',
    'twitter': 'https://twitter.com/poornasri26'
}

# Current Focus Areas
FOCUS_AREAS = [
    'AI/ML Research - Building intelligent systems that understand and adapt to human behavior',
    'Gamification - Creating engaging experiences that make productivity fun',
    'Blockchain - Developing decentralized solutions for real-world problems',
    'Open Source - Contributing to tools that make developers\' lives better'
]

# Barbie Theme Colors
BARBIE_THEME = {
    'primary': '#E91E63',      # Hot pink
    'secondary': '#F48FB1',    # Light pink
    'accent': '#CE93D8',       # Purple
    'background': '#FFFFFF',   # White
    'text': '#880E4F',         # Dark pink
    'dark': '#4A148C'          # Purple
}

# Repository Categories
REPO_CATEGORIES = {
    'AI Research': ['ai', 'ml', 'machine', 'learning', 'neural', 'deep', 'cognitive', 'eeg', 'fusion'],
    'Gaming': ['game', 'geo', 'shape', 'multiplayer', 'guess'],
    'Education': ['sort', 'algorithm', 'visualizer', 'learn', 'tutorial'],
    'Networking': ['network', 'router', 'lab', 'adaptive'],
    'ML': ['spam', 'detector', 'classification', 'email'],
    'Blockchain': ['blockchain', 'voting', 'smart', 'contract', 'web3'],
    'NLP': ['spell', 'telugu', 'language', 'nlp', 'search'],
    'Featured': ['solo', 'quest', 'productivity', 'rpg']
}

# Featured Repositories (will be displayed prominently)
FEATURED_REPOS = [
    'solo-quest',
    'Cogni-Fusion',
    'telugu_spell_index',
    'GeoShape'
]

# Skills by Category
SKILLS = {
    'Languages': ['TypeScript', 'JavaScript', 'Python', 'Solidity', 'Rust', 'Go', 'Java'],
    'Web Development': ['React', 'Next.js', 'Node.js', 'Express.js', 'Vite', 'Tailwind CSS', 'Svelte'],
    'Data & Core': ['Prisma', 'SQLite', 'MongoDB', 'PostgreSQL'],
    'AI/ML & Research': ['PyTorch', 'TensorFlow', 'FastAPI', 'Scikit-learn', 'NLTK'],
    'Cloud & DevOps': ['AWS', 'Docker', 'Kubernetes', 'Terraform', 'Linux', 'Git'],
    'Blockchain': ['Ethereum', 'Hardhat', 'Web3.js']
}

# Automation Settings
AUTOMATION_CONFIG = {
    'update_frequency': 'daily',  # daily, weekly, monthly
    'max_repos_display': 12,     # Maximum number of repos to display
    'include_forks': False,      # Whether to include forked repositories
    'include_archived': False,   # Whether to include archived repositories
    'error_check_enabled': True, # Whether to run error checks
    'banner_generation': True     # Whether to generate custom banner
}