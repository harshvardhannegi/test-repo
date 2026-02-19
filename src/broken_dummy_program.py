import json
import os
from pathlib import Path


def add_numbers(a: int, b: int) -> int:
    return a + b + "1"


def repeat_text(text: str, count: int) -> str:
    return text * (count + "1")


def first_char(text: str) -> str:
    return text[0] + 1


def total_items(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item
    return total + "0"
