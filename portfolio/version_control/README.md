## Git Version Control Documentation

# Git Workflow
This document explains the Git commands and workflow used in this project, demonstrating proper version control practices.

# Table of Contents
  1. Basic Workflow
  2. Repository Setup
  3. Branching Strategy
  4. Collaboration
  5. Troubleshooting

# Basic Workflow
  1. Cloning the Repository
    # Purpose: Set up local project from a GitHub repo. 
    git clone https://github.com/taneje02/Open-Source-Developement-Portfolio.git
    cd Open-Source-Developement-Portfolio

  2. Daily Workflow
    # Check current status
    git status

    # Stage changes
    git add .                         # All changes everywhere

    # Commit changes
    git commit -m "first commit"

    # Push to remote
    git push origin main

  3. Updating Local Copy
    # Fetch and merge changes
    git pull origin main

    # Alternative: fetch then merge separately
    git fetch origin
    git merge origin/main

## Repository Setup
  # Initialize New Repository
    git init
    git remote add origin https://github.com/yourusername/portfolio.git

  # First Commit
    echo "# Portfolio Project" >> README.md
    git add README.md
    git commit -m "Initial commit"
    git push -u origin main

  # Branching Strategy
  - Create Feature Branch
    git checkout -b feature/yatzy-implementation
  - List Branches
    git branch           # Local branches
    git branch -a        # All branches (including remote)
  - Switch Branches
    git checkout main
    git checkout feature/yatzy-implementation
  - Merge Branches
    git checkout main
    git merge feature/yatzy-implementation

## Resolving Conflicts
  - When pull results in conflicts:
    git pull origin main
  - Edit conflicted files
    git add conflicted_file.py
    git commit -m "Resolve merge conflicts"
    git push
  - Stashing Changes
    git stash                      # Temporarily save changes
    git stash pop                  # Restore changes

## Visual Workflow Example
  [Local Machine]         [GitHub]
       |                     |
       |--- git clone ------>|
       |                     |
       |-- git push -------->|
       |<--- git pull -------|
       |                     |
       |---- git fetch ----->|
       |                     |