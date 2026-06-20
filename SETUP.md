# GitHub Profile README Setup Guide

## Quick Start

1. **Create a new repository on GitHub**
   - Go to https://github.com/new
   - Repository name: `PoornaSri26` (must match your username)
   - Make it **Public**
   - Initialize with a README (optional, will be replaced)
   - Click "Create repository"

2. **Push your local files to GitHub**
   ```bash
   cd C:\Users\npoor\CascadeProjects\PoornaSri26
   git init
   git add .
   git commit -m "Initial commit: High-end techy profile README"
   git branch -M main
   git remote add origin https://github.com/PoornaSri26/PoornaSri26.git
   git push -u origin main
   ```

3. **Enable GitHub Actions**
   - Go to your repository on GitHub
   - Navigate to **Settings** → **Actions** → **General**
   - Under "Actions permissions", select "Allow all actions and reusable workflows"
   - Click Save

4. **Customize your profile**
   - Edit `README.md` to update:
     - Your tech stack badges
     - "Currently" section with your actual projects
     - Social media links in the Connect section
   - Update the GitHub Actions workflow if needed

## Features Included

- **Terminal-style intro** with neofetch aesthetic
- **Dynamic GitHub stats** with transparent theme
- **Tech stack badges** with flat, elegant styling
- **Collapsible sections** for detailed stats and connections
- **GitHub Actions** for automatic activity updates
- **Dark/light mode compatible** via transparent themes

## Customization Options

### Update Tech Stack
Replace the badge URLs in the "Tech & Tools" section with your actual technologies:
```markdown
![YourSkill](https://img.shields.io/badge/-YourSkill-COLOR?style=flat&logo=your-skill&logoColor=white)
```

### Update Social Links
Replace the URLs in the "Connect & Support" section with your actual profiles.

### Add Blog Posts
To add dynamic blog posts, you can use the [blog-post-workflow](https://github.com/gautamkrishnar/blog-post-workflow) action. Add this to your workflow file.

### Add Spotify Now Playing
Use [novatorem](https://github.com/novatorem/novatorem) to add a Spotify "Now Playing" card.

## Design Principles Applied

- ✅ Minimal, focused content above the fold
- ✅ Transparent themes for seamless integration
- ✅ Terminal aesthetic for techy feel
- ✅ Collapsible sections to reduce clutter
- ✅ Automated updates via GitHub Actions
- ✅ No distracting GIFs or excessive emojis
- ✅ Consistent color scheme (indigo #6366f1)

## Next Steps

1. Push to GitHub
2. Verify the README renders correctly in both light and dark mode
3. Watch the GitHub Actions run automatically
4. Iterate and refine based on your personal brand

## Resources

- [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats)
- [Streak Stats](https://github.com/DenverCoder1/github-readme-streak-stats)
- [Shields.io](https://shields.io/)
- [Awesome GitHub Profile READMEs](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
