"""Auxiliary functions related to the Fibonacci sequence."""
from collections import deque
from typing import Generator


def fibonacci(n: int = -1) -> Generator[int, None, None]:
    """Yield the first n Fibonacci numbers.
       Generates infinitely if n is negative."""
    a, b = 0, 1
    if n < 0 or n >= 1:
        yield a
    if n < 0 or n >= 2:
        yield b
    i = 2
    while n < 0 or i < n:
        c = a + b
        yield c
        a, b = b, c
        i += 1


def fibonacci_upto(n: int) -> Generator[int, None, None]:
    """Yield the Fibonacci numbers smaller than n."""
    a, b = 0, 1
    if a < n:
        yield a
    if b < n:
        yield b
    while True:
        c = a + b
        if c >= n:
            return
        yield c
        a, b = b, c


def nth_fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number, starting at index 0.
       Running the recursion is faster than calculating Binet's formula.
       Raises ValueError if n is negative."""
    if n < 0:
        raise ValueError('Negative parameter')
    return deque(fibonacci(n + 1), maxlen=1)[-1]


# TODO:
# Implement the log n time algorithm based on matrix multiplication!
# https://muthu.co/fast-nth-fibonacci-number-algorithm/
