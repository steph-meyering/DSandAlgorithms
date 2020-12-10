class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(1, len(prices)):
            max_prof = max(max_prof, prices[i] - prices[i-1] + max_prof)
        return max_prof
