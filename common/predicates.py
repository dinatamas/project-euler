"""Simple predicate functions for deciding and filtering."""
def is_even(n: int) -> bool:
    return n % 2 == 0


def is_odd(n: int) -> bool:
    return n % 2 == 1


def is_palindrome(n: int) -> bool:
    """Decide if a number is the same backwards."""
    return str(n) == str(n)[::-1]


def ispalindrome2(n, b):
    reversed = 0
    k = n
    while k > 0:
        reversed = b * reversed + k % b
        k = k // b
    return (n == reversed)


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    return a ** 2 + b ** 2 == c ** 2
