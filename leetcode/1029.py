class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        price_diff = [(x[0] - x[1]) for x in costs]
        sorted_costs = [ x for _, x in sorted(zip(price_diff, costs))]
        for i, pair in enumerate(sorted_costs):
            if i < len(sorted_costs)/2:
                res += pair[0]
            else:
                res += pair[1]
        return res