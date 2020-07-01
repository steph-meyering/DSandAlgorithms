class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy_min = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy_min)
            buy_min = min(buy_min, prices[i])
        return profit
