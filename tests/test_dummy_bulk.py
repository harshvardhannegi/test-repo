import pytest

from src import broken_dummy_program as app


@pytest.mark.parametrize(
    "a,b",
    [
        (11, 12),
        (14, 9),
        (100, 1),
        (7, 7),
        (9, 1),
        (13, 3),
        (21, 4),
        (18, 2),
        (33, 3),
        (41, 1),
        (6, 6),
        (12, 12),
        (15, 5),
        (19, 1),
        (22, 2),
    ],
)
def test_bulk_add_numbers_type_errors(a, b):
    with pytest.raises(TypeError):
        app.add_numbers(a, b)


@pytest.mark.parametrize(
    "text,count",
    [
        ("n", 2),
        ("p", 5),
        ("xy", 3),
        ("r", 1),
        ("ab", 2),
        ("m", 4),
        ("q", 6),
        ("w", 3),
        ("uv", 2),
        ("t", 7),
        ("d", 8),
        ("k", 9),
        ("v", 10),
        ("h", 11),
        ("j", 12),
    ],
)
def test_bulk_repeat_text_type_errors(text, count):
    with pytest.raises(TypeError):
        app.repeat_text(text, count)
