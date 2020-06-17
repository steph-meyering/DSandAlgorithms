class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_pointer = 0
        two_pointer = len(nums) - 1
        i = 0
        while i <= two_pointer:
            if nums[i] == 0:
                nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
                zero_pointer += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two_pointer] = nums[two_pointer], nums[i]
                two_pointer -= 1
            else:
                i += 1
                
        