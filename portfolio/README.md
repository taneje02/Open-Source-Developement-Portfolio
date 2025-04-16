# Yatzy Game

This is a simplified implementation of the Yatzy game written in Python. It includes:

## Features
- Yatzy class with 5 dice that can be rolled and locked individually.
- Scoring methods for Ones to Sixes, OnePair, TwoPairs, ThreeAlike, FourAlike, Small/Large straights, Full House, Chance, and Yatzy.
- Unit tests using `unittest`.
- GitHub Actions integration for CI.

## Structure

portfolio/
|── version_control/
|   ├── screenshots/         # GitHub CLI or GUI screenshots showing add, commit, push, etc.
|   └── README.md           # Explanation of version control commands Git commands and workflow
|
├── yatzy_game/
|   ├── yatzy.py            # The main Yatzy class
|   ├── test_yatzy.py       # Unit tests for all scoring methods
|   ├── game_demo.py        # A simple script showing gameplay & scoring options
|   ├── README.md           # Documentation
|   └── python-app.yml      # GitHub Actions workflow
|
|── github_issues/
│   ├── issue_report.md     # documentation of issues found
│   ├── fixes/              # code changes made to address issues
│   └── screenshots/        # Screenshots showing issue creation, discussion, fix, and merge
│
|── .gitignore              # Ignore python caches
└── README.md               # Main guide to your portfolio structure


## Usage
```bash
python game_demo.py
```

## Run Tests
```bash
python -m unittest discover
```

## GitHub Actions
Push or open a pull request on `main` to run automated tests.
