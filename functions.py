import re

# is_palindrome


def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


# fibonacci


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# count_vowels


def count_vowels(text: str) -> int:
    vowels = "aeiouyąęó"
    return sum(1 for char in text.lower() if char in vowels)


# calculate_discount


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError("discount must be between 0 and 1")

    return price * (1 - discount)


# flatten_list


def flatten_list(nested_list: list) -> list:
    result = []

    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


# word_frequencies


def word_frequencies(text: str) -> dict:
    words = re.findall(r"\b\w+\b", text.lower())
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


# is_prime


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
