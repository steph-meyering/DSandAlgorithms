class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        op = 0
        cl = 0
        for c in S:
            if c == "(":
                op += 1
            elif op > 0:
                op -= 1
            else:
                cl += 1
        return op + cl
