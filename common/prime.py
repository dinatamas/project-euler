"""Utilities for dealing with prime numbers."""
import itertools
from math import ceil, floor, log
from typing import Generator


def primes(n: int = -1) -> Generator[int, None, None]:
    """Yield the first n primes.
       Generates infinitely if n is negative.
       Implements the sieve of Erathosthenes by the Python Cookbook."""
    # TODO: https://stackverflow.com/a/10733621
    D = {}
    if n >= 1:
        yield 2
    primes_found = 1
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        if primes_found >= n:
            return
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
            primes_found += 1
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p


def primes_upto(n: int) -> Generator[int, None, None]:
    """Generate the primes smaller than n."""
    yield from itertools.takewhile(lambda p: p < n, primes(n))


def prime_count_lower_bound(n: int) -> int:
    """Return a lower bound on the number of primes smaller than n."""
    return ceil(n / log(n))


def prime_count_upper_bound(n: int) -> int:
    """Return an upper bound on the number of primes smaller than n."""
    return floor(1.25506 * n / log(n))


# TODO:
# There are many great prime generating algorithms.
# https://stackoverflow.com/a/2068548
# A more efficient solution should be implemented.

# TODO:
# Closer bounds on the prime count exist!
