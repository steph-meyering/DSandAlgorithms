class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            nums[val] = -abs(nums[val])
        return [i+1 for i, num in enumerate(nums) if num >= 0]