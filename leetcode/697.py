class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = dict()
        max_freq = 0
        min_len = len(nums)
        for i, n in enumerate(nums):
            if n not in freq:
                freq[n] = []
            freq[n].append(i)
            max_freq = max(max_freq, len(freq[n]))

        ans = len(nums)
        for k in freq:
            if len(freq[k]) == max_freq:
                ans = min(ans, freq[k][-1] - freq[k][0] + 1)
        return ans
