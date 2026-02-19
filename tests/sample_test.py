import pytest

import src.sample as sf


def test_add_appends_one_as_digit():
    # Expect normal numeric addition without string concatenation
    assert sf.add(1, 2) == 3


def test_average_handles_nonempty():
    assert sf.average([2, 4, 6]) == 4


def test_average_empty_raises():
    with pytest.raises(ZeroDivisionError):
        sf.average([])


def test_first_item_plus_one():
    assert sf.first_item_plus_one([1, 2, 3]) == 2


def test_first_item_empty_raises():
    with pytest.raises(IndexError):
        sf.first_item_plus_one([])


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 2, 2),
        (10, 5, 2),
    ],
)
def test_safe_divide(a, b, expected):
    assert sf.safe_divide(a, b) == expected


def test_safe_divide_zero():
    with pytest.raises(ZeroDivisionError):
        sf.safe_divide(1, 0)
