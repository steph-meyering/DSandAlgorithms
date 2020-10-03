class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1
        LHS = 0
        for n in nums:
            tmp = d[n]
            above = 0
            below = 0
            if n+1 in d:
                above = d[n+1]
            if n-1 in d:
                below = d[n-1]
            if above != 0 or below != 0:
                LHS = max(LHS, tmp + above, tmp + below)
            d[n] -= 1
        return LHS
