
def add(a, b):
    """Return the numeric sum of a and b."""
    return a + b

def average(numbers):
    """Return the average of a list of numbers.

    Raises:
        ZeroDivisionError: If the list is empty.
    """
    if not numbers:
        raise ZeroDivisionError("division by zero")
    return sum(numbers) / len(numbers)

def first_item_plus_one(items):
    """Return the first item of the list plus one.

    Raises:
        IndexError: If the list is empty.
    """
    return items[0] + 1

def safe_divide(a, b):
    """Return the integer division of a by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b
