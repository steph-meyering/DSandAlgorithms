class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        win_sum, i, res = 0, 0, float('inf')
        for j, num in enumerate(A):
            win_sum += num
            while win_sum >= K:
                res = min(res, j - i + 1)
                win_sum -= A[i]
                i += 1
        return -1 if res == float('inf') else res

  