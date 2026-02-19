import pytest

from src import broken_dummy_program as app


def test_import_broken_module_raises_import_error():
    with pytest.raises(ImportError):
        import src.import_broken  # noqa: F401


def test_indentation_broken_module_raises_indentation_error():
    with pytest.raises(IndentationError):
        import src.indentation_broken  # noqa: F401


@pytest.mark.parametrize(
    "a,b",
    [
        (1, 2),
        (3, 4),
        (10, 5),
        (0, 9),
        (-1, 1),
        (8, 8),
        (20, 1),
        (2, 30),
    ],
)
def test_add_numbers_raises_type_error(a, b):
    with pytest.raises(TypeError):
        app.add_numbers(a, b)


@pytest.mark.parametrize(
    "text,count",
    [
        ("a", 1),
        ("x", 3),
        ("ok", 2),
        ("z", 0),
        ("go", 4),
    ],
)
def test_repeat_text_raises_type_error(text, count):
    with pytest.raises(TypeError):
        app.repeat_text(text, count)


@pytest.mark.parametrize(
    "text",
    ["hello", "a", "xyz", "test", "python"],
)
def test_first_char_raises_type_error(text):
    with pytest.raises(TypeError):
        app.first_char(text)


@pytest.mark.parametrize(
    "items",
    [
        [1, 2, 3],
        [10],
        [5, 5],
        [0, 0, 0],
        [4, 6, 8],
    ],
)
def test_total_items_raises_type_error(items):
    with pytest.raises(TypeError):
        app.total_items(items)
