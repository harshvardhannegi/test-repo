import pytest

from src import broken_dummy_program as app


def test_divide_exact():
    assert app.divide(8, 2) == 4.0


def test_divide_fraction():
    assert app.divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        app.divide(4, 0)


def test_parse_number_string():
    assert app.parse_number("10") == 11


def test_parse_number_float_string():
    assert app.parse_number("3.0") == 3


def test_greet_format():
    assert app.greet("Ana") == "Hello Ana"


def test_config_value_present():
    assert app.config_value({"env": "prod"}, "env") == "prod"


def test_config_value_missing_default():
    assert app.config_value({}, "env") is None


def test_join_words_basic():
    assert app.join_words(["a", "b", "c"]) == "a b c"


def test_join_words_empty():
    assert app.join_words([]) == ""


def test_is_even_true():
    assert app.is_even(4) is True


def test_is_even_false():
    assert app.is_even(5) is False


def test_parse_number_none():
    with pytest.raises(TypeError):
        app.parse_number(None)


def test_divide_negative_values():
    assert app.divide(-9, 3) == -3


def test_join_words_numbers():
    assert app.join_words(["1", "2"]) == "1,2"
