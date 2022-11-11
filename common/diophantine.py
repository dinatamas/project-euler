"""Polynomials and utilities with integer focus."""
from math import sqrt
from typing import Optional


def make_pythagorean_triplet(a: int, b: int) -> Optional[int]:
    """Finds c when given a and b in: a^2 + b^2 = c^2.
       Returns None if c is not an integer."""
    # TODO: Handle negative and zero cases!
    # TODO: Allow keyword args and passing c as well!
    c = sqrt(a ** 2 + b ** 2)
    if c == int(c):
        return int(c)
    else:
        return None
