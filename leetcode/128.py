class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                cur_streak = 1
                cur_num = n
                while n + 1 in nums_set:
                    cur_streak += 1
                    n += 1
                max_streak = max(max_streak, cur_streak)
        return max_streak
