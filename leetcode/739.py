class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for i in T]
        for i, temp in enumerate(T):
            while stack and stack[-1][0] < temp:
                t, j = stack.pop()
                res[j] = i - j
            stack.append((temp, i))

        return res
