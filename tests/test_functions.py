# tests for is_palindrome

from functions import is_palindrome, fibonacci, count_vowels


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

# tests for fibonacci

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

# tests for count_vowels

def test_count_vowels_python():
    assert count_vowels("Python") == 2


def test_count_vowels_all_vowels():
    assert count_vowels("AEIOUY") == 6


def test_count_vowels_no_vowels():
    assert count_vowels("bcd") == 0


def test_count_vowels_empty_string():
    assert count_vowels("") == 0


def test_count_vowels_polish_chars():
    assert count_vowels("Próba żółwia") == 5
