"""10001st prime"""
from collections import deque
from common.prime import primes


print(deque(primes(10001), maxlen=1)[-1])
