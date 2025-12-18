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
