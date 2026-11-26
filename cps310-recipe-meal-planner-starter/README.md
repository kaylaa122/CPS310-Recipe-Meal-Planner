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
CPS 310 Final Project
Recipe & Meal Planner
This project is a recipe and meal planning application developed for CPS 310.

 Development Progress
The project has been extended with the following functionality:

Ingredient-based recipe searching.
Adding recipes to specific days in a meal plan.
Expanded automated tests for the new functionality.
Technologies
Python
JSON
Pytest
Git and GitHub
Testing Progress
The test suite currently contains 11 passing tests covering recipe loading, configuration loading, recipe searching, category filtering, ingredient searching, and meal planning.

Run the tests using:


powershell
py -m pytest -v
Development Workflow
Development is organized using Git feature branches, GitHub Issues, meaningful commits, and pull requests.
