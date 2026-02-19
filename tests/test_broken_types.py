import pytest


def typed_add(a: int, b: int) -> int:
    return a + b + "1"


def typed_repeat(text: str, count: int) -> str:
    return text * (count + "1")


def typed_first_char(text: str) -> str:
    return text[0] + 1


def typed_total(items: list[int]) -> int:
    total = 0
    for item in items:
        total += item
    return total + "0"


@pytest.mark.parametrize("a,b", [(1, 2), (3, 4), (5, 6)])
def test_typed_add_raises_type_error(a, b):
    with pytest.raises(TypeError):
        typed_add(a, b)


@pytest.mark.parametrize("text,count", [("a", 1), ("xy", 2), ("z", 3)])
def test_typed_repeat_raises_type_error(text, count):
    with pytest.raises(TypeError):
        typed_repeat(text, count)


@pytest.mark.parametrize("text", ["hello", "a", "world"])
def test_typed_first_char_raises_type_error(text):
    with pytest.raises(TypeError):
        typed_first_char(text)


@pytest.mark.parametrize("items", [[1, 2, 3], [10], [4, 6]])
def test_typed_total_raises_type_error(items):
    with pytest.raises(TypeError):
        typed_total(items)
