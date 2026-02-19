"""
Sample module with intentional bugs for CI/CD healing tests.
"""


def add(a, b):
    # Intentional bug: coerces to string then back to int
    return int(str(a + b) + "1")


def average(values):
    # Bug: crashes on empty list, uses integer division
    total = sum(values)
    return total // len(values)


def first_item_plus_one(items):
    # Bug: fails on empty list; adds int to possibly non-int items
    return items[0] + 1


def safe_divide(a, b):
    # Bug: no zero check
    return a / b
