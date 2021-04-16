class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for i in range(1, len(nums)):
            prev = res[-1]
            res.append(prev + nums[i])
        return res