# Yatzy Game Implementation

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Tests](https://github.com/yourusername/yatzy/actions/workflows/python-app.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

A Python implementation of the classic Yatzy dice game scoring system, designed as part of a university portfolio assignment.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Class Documentation](#class-documentation)
- [Testing](#testing)
- [GitHub Actions](#github-actions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Complete Yatzy scoring system implementation
- Individual dice locking mechanism
- All standard Yatzy scoring methods:
  - Single number scores (Ones through Sixes)
  - One Pair, Two Pairs
  - Three-of-a-kind, Four-of-a-kind
  - Small Straight, Large Straight
  - Full House
  - Chance
  - Yatzy (five-of-a-kind)
- Automated testing via GitHub Actions
- Comprehensive unit test coverage

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/yatzy.git
   cd yatzy

2. Set up a virtual environment (recommended):
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

## Usage

 - Basic Usage
    from yatzy import Yatzy

    # Create a new game
    game = Yatzy()

    # Roll the dice
    game.roll()

    # Lock specific dice (0-4)
    game.lock_die(0)
    game.lock_die(1)

    # Roll again (only unlocked dice will change)
    game.roll()

    # Calculate scores
    print("Ones score:", game.ones())
    print("Three-of-a-kind:", game.three_alike())    

## Mock Game Example
    Run the included mock game:
    python game_mockup.py