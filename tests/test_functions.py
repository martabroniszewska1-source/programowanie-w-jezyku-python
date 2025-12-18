# tests for is_palindrome

from functions import is_palindrome, fibonacci


def test_kajak():
    assert is_palindrome("kajak") is True


def test_sentence():
    assert is_palindrome("Kobyła ma mały bok") is True


def test_not_palindrome():
    assert is_palindrome("python") is False


def test_empty_string():
    assert is_palindrome("") is True


def test_single_character():
    assert is_palindrome("A") is True

#tests for fibonacci

import pytest


def test_fibonacci_0():
    assert fibonacci(0) == 0


def test_fibonacci_1():
    assert fibonacci(1) == 1


def test_fibonacci_5():
    assert fibonacci(5) == 5


def test_fibonacci_10():
    assert fibonacci(10) == 55


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)
