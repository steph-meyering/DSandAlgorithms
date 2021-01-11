import unittest

# RECURSIVE W/ MEMOIZATION O(n) time and O(n) space for call stack

# def fib(n, memo = {0: 0, 1: 1}):
#     # Compute the nth Fibonacci number
#     if n < 0:
#         raise Exception('sequence index must be non-negative')
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fib(n-1) + fib(n-2)
        
#     return memo[n]

# ITERATIVE O(n) time and O(1) space
def fib(n):
    # Compute the nth Fibonacci number
    if n < 0:
        raise Exception('sequence index must be non-negative')
    if n < 2:
        return n
    prev1 = 0
    prev2 = 1
    for i in range(2, n+1):
        fib_num = prev1 + prev2
        prev1, prev2 = prev2, fib_num
    return prev2














# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
