"""Largest palindrome product"""
from common.predicates import is_palindrome


result = 0
for n in range(100, 999):
    for m in range(100, 999):
        if is_palindrome(n * m) and n * m > result:
            result = n * m
print(result)
