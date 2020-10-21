class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1]  # [1,1,2,6]
        rprod = 1  # [24,12,4,1]
        for i in range(1, len(nums)):
            lprod.append(lprod[-1] * nums[i-1])
        for j in range(len(nums)-1, -1, -1):
            lprod[j] *= rprod
            rprod *= nums[j]
        return lprod
