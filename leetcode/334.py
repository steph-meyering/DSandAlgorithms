class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float('inf'), float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        for i in range(l-2):
            for j in range(i+1, l-1):
                if nums[i] < nums[j]:
                    for k in range(j+1, l):
                        if nums[j] < nums[k]:
                            return True
        return False
