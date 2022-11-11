"""Highly divisible triangular number"""
from itertools import count

from common.factorization import divisors, factorize


triangle_number = 0
for i in count(1):
    triangle_number += i
    if len(divisors(triangle_number)) > 500:
        print(triangle_number)
        break
