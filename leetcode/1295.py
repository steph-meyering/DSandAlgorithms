class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if 10 <= num <= 99 or 1000 <= num <= 9999 or 100000 == num:
                res += 1
        return res
