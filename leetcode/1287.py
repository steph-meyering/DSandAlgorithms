class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)
        last_1, res = None, 0
        for i in range(2, len(b)):
            if last_1:
                if b[i] == "1":
                    res = max(res, i - last_1)
                    last_1 = i
            elif b[i] == "1":
                last_1 = i
        return res
