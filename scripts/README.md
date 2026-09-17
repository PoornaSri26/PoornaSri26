# GitHub Profile Automation Scripts

This directory contains automation scripts for keeping your GitHub profile updated with the latest repositories and generating personalized content.

## Scripts Overview

### 1. `update_profile.py`
Automatically updates your GitHub profile README with:
- Latest repositories from your GitHub account
- Categorized project tables
- Updated statistics (repo count, stars)
- Dynamic project descriptions

### 2. `generate_banner.py`
Creates a personalized Barbie-themed banner with:
- Your name and role
- Current focus areas
- Featured projects
- Tech stack information
- Status indicators
- Radar-style graphics

### 3. `error_check.py`
Performs comprehensive error checking:
- Validates repository links
- Checks image links
- Verifies markdown syntax
- Confirms repository existence
- Generates detailed error reports

### 4. `config.py`
Centralized configuration for:
- User information
- Theme colors
- Repository categories
- Featured repositories
- Skills and focus areas
- Automation settings

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure GitHub token (optional but recommended):
- Go to GitHub Settings → Developer settings → Personal access tokens
- Generate a new token with `repo` scope
- Add it as a secret in your repository settings: `GITHUB_TOKEN`

3. Customize your profile in `config.py`:
- Update user information
- Modify theme colors
- Add repository categories
- Set featured repositories

## Usage

### Manual Testing
```bash
# Test individual scripts
python update_profile.py
python generate_banner.py
python error_check.py
```

### Automated Updates
The automation runs automatically via GitHub Actions:
- **Daily**: At midnight UTC
- **On push**: When you push to main branch
- **Manual**: Via workflow dispatch

## Features

### Auto-Update Features
- Detects new repositories automatically
- Categorizes projects intelligently
- Updates statistics in real-time
- Maintains consistent formatting

### Barbie Theme
- Hot pink and purple color scheme
- Gradient backgrounds
- Decorative elements
- Professional yet playful design

### Error Checking
- Comprehensive link validation
- Markdown syntax checking
- Repository existence verification
- Detailed error reporting

## Customization

### Theme Colors
Edit `BARBIE_THEME` in `config.py`:
```python
BARBIE_THEME = {
    'primary': '#E91E63',      # Hot pink
    'secondary': '#F48FB1',    # Light pink
    'accent': '#CE93D8',       # Purple
    # ... more colors
}
```

### Repository Categories
Add custom categories in `config.py`:
```python
REPO_CATEGORIES = {
    'Your Category': ['keyword1', 'keyword2']
}
```

### Featured Repositories
Update the list in `config.py`:
```python
FEATURED_REPOS = [
    'your-repo-name',
    'another-repo'
]
```

## Troubleshooting

### Scripts not running
- Check Python version (requires 3.10+)
- Ensure dependencies are installed
- Verify GitHub token permissions

### Banner not generating
- Check Pillow installation
- Verify font availability
- Ensure assets directory exists

### Links not updating
- Verify GitHub token has proper scope
- Check API rate limits
- Ensure repository is public

## Workflow

The GitHub Actions workflow:
1. Checks out your repository
2. Sets up Python environment
3. Installs dependencies
4. Runs profile update script
5. Generates personalized banner
6. Performs error checking
7. Commits and pushes changes

## Contributing

To add new automation features:
1. Create a new script in this directory
2. Add dependencies to `requirements.txt`
3. Update the workflow in `.github/workflows/auto-update.yml`
4. Document the feature in this README

## License

This automation is part of your GitHub profile and follows the same license as your main repository.