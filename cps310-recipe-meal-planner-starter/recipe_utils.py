"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]
def search_by_ingredient(recipes, ingredient_name):
    """Return recipes that contain the requested ingredient."""
    ingredient_name = ingredient_name.lower().strip()

    return [
        recipe
        for recipe in recipes
        if any(
            ingredient_name in ingredient["name"].lower()
            for ingredient in recipe["ingredients"]
        )
    ]
