class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = 0
        for n in nums:
            b = n ^ b
        return b
