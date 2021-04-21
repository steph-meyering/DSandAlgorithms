class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for val in count.values():
            if val >= 2:
                res += ((val-1) ** 2 + val-1)//2
        return res