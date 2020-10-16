class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        for i in range(3, len(b)):
            if b[i] == b[i-1]:
                return False
        return True
