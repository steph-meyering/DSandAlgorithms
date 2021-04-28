# sorting

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        for bar_cost in sorted(costs):
            coins -= bar_cost
            if coins >= 0:
                bars += 1
            else:
                return bars
        return bars