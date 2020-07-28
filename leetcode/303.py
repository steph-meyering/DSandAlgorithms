class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]
        for i, n in enumerate(nums):
            self.dp.append(n + self.dp[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
