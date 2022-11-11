"""Even Fibonacci numbers"""
from common.fibonacci import fibonacci_upto
from common.predicates import is_even


print(sum(filter(is_even, fibonacci_upto(4000001))))
