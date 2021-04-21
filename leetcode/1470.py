class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = int(len(nums) / 2)
        i, j = 0, n
        res = []
        for _ in range(n):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res