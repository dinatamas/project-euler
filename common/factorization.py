"""Algorithms for finding prime factors and divisors."""
from itertools import combinations, count
from math import gcd, prod
from typing import Generator


# TODO: Generator?
# TODO: Negative numbers, zero?
def factorize(n: int) -> list[int]:
    """Pollard's rho algorithm to produce prime factors."""
    def _get_next_factor() -> int:
        if n % 2 == 0:
            return 2
        x = 2
        for cycle in count(1):
            y = x
            for _ in range(2 ** cycle):
                x = (x * x + 1) % n
                factor = gcd(x - y, n)
                if factor > 1:
                    return factor
    factors = []
    while n != 1:
        factor = _get_next_factor()
        factors.append(factor)
        n //= factor
    return sorted(factors)


def divisors(n: int) -> Generator[int, None, None]:
    """Yield the divisors of an intenger."""
    factors = factorize(n)
    divisors = set([1])
    for r in range(1, len(factors) + 1):
        divisors.update(map(prod, combinations(factors, r)))
    return sorted(divisors)


# TODO:
# Pollard's rho method is easy to implement, but less efficient
# for large numbers than say the Quadratic Sieve. At a later time
# it should be considered to reimplement factorize() with that.
# https://github.com/cramppet/quadratic-sieve/blob/master/QS.py
# https://ieeexplore.ieee.org/document/7556107
# Wheel factorization could also be considered.
