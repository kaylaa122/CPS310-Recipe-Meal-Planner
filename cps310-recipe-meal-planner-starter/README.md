# CPS 310 Final Project Starter
## Recipe & Meal Planner

This repository contains the starter code for the CPS 310 final project.

The application currently supports:

- loading recipe data from JSON
- listing all recipes
- searching recipes by name
- filtering recipes by category
- viewing recipe details
- loading basic configuration from `config.json`

This is intentionally a **starter project**, not a finished application.

## Setup

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```

## Run Tests

### Windows

```powershell
python -m pytest -v
```

### macOS

```bash
python3 -m pytest -v
```

You are expected to make your own design decisions as you extend the project during the final project. 

Checkpoint 1 Progress
Completed Features
Search recipes by name
Filter recipes by category
Search recipes by ingredient
Development Workflow
Created GitHub Issues for planned work
Developed features on separate branches
Created and merged pull requests
Added and maintained pytest tests
Testing Status
All current tests are passing.

Planned Features
Weekly meal planning
Additional test coverage
