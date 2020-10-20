class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.exact = False
        self.res = sum(nums[:3])
        for i in range(len(nums)):
            if self.exact:
                return self.res
            if i == 0 or nums[i] != nums[i-1]:
                self.two_sum(nums, nums[i], target, i)
        return self.res
        
    def two_sum(self, nums, numi, target, i):
        i, j = i + 1, len(nums) - 1
        while i < j:
            cur_sum = nums[i] + nums[j] + numi
            if cur_sum - target == 0:
                self.exact = True
                self.res = cur_sum
                return
            if abs(cur_sum - target) < abs(self.res - target):
                self.res = cur_sum
            if cur_sum - target < 0:
                i += 1
            else:
                j -= 1
