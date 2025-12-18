# tests for is_palindrome

import pytest

from functions import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


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


# tests for calculate_discount


def test_calculate_discount_standard():
    assert calculate_discount(100, 0.2) == 80.0


def test_calculate_discount_zero():
    assert calculate_discount(50, 0) == 50.0


def test_calculate_discount_full():
    assert calculate_discount(200, 1) == 0.0


def test_calculate_discount_negative():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)


def test_calculate_discount_too_high():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


# tests for flatten_list


def test_flatten_simple():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]


def test_flatten_nested():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_flatten_empty():
    assert flatten_list([]) == []


def test_flatten_deep_nested():
    assert flatten_list([[[1]]]) == [1]


def test_flatten_mixed():
    assert flatten_list([1, 2, [3, [4]]]) == [1, 2, 3, 4]


# tests for word_frequencies


def test_word_frequencies_basic():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }


def test_word_frequencies_punctuation():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}


def test_word_frequencies_case_insensitive():
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_polish_sentence():
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {
        "ala": 1,
        "ma": 2,
        "kota": 1,
        "a": 1,
        "kot": 1,
        "ale": 1,
    }


# tests for is_prime
def test_is_prime_2():
    assert is_prime(2) is True


def test_is_prime_3():
    assert is_prime(3) is True


def test_is_prime_4():
    assert is_prime(4) is False


def test_is_prime_0():
    assert is_prime(0) is False


def test_is_prime_1():
    assert is_prime(1) is False


def test_is_prime_5():
    assert is_prime(5) is True


def test_is_prime_97():
    assert is_prime(97) is True
