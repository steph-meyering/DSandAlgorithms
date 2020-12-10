class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        fact = 1
        if x < 0:
            x *= -1
            fact *= -1
        while x > 0:
            res *= 10
            res += (x % 10)
            x = x//10
        if res >= 2147483648:
            return 0
        return res * fact
