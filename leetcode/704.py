class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo)//2)
            diff = target - nums[mid]
            if diff == 0:
                return mid
            elif diff < 0:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
