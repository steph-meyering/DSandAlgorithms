class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        return max([sum(c) for c in accounts])