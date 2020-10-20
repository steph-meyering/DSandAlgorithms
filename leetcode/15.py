class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.two_sum(nums, -nums[i], i+1, res)
        return res
        
    def two_sum(self, nums, target, i, res):
        j = len(nums) - 1
        while i < j:
            cur_sum = nums[i] + nums[j]
            if cur_sum == target:
                res.append([-target, nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            elif cur_sum < target:
                i += 1
            else:
                j -= 1