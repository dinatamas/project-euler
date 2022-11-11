"""Special Pythagorean triplet"""
from sys import exit

from common.diophantine import make_pythagorean_triplet


for a in range(1, 1000):
    for b in range(1, 1000):
        if c := make_pythagorean_triplet(a, b):
            print(a, b, c)
            if a + b + c == 1000:
                print(a * b * c)
                exit()
