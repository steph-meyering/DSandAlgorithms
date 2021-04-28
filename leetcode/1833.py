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


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = Counter(costs)
        res = 0
        for i in range(10**5 + 1):
            if i in counter:
                while counter[i] > 0:
                    counter[i] -= 1
                    coins -= i
                    if coins >= 0:
                        res += 1
                    else:
                        return res
        return res