class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_freq = {}
        for i, num in enumerate(sorted_nums):
            if num not in num_freq:
                num_freq[num] = i

        for i, num in enumerate(nums):
            sorted_nums[i] = num_freq[num]

        return sorted_nums
