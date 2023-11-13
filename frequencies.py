"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if not isinstance(item, str):
            frequencies[item] = str(item)
        frequencies[item] = items.count(item)
    return frequencies
