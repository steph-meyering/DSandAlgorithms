class Solution:
    def shortestSubarray(self, A, K):
        win_sum, i, res = 0, 0, float('inf')
        last_neg_i = -1
        for j, num in enumerate(A):
            if num <= 0:
                last_neg_i = j
            win_sum += num
            while win_sum >= K:
                res = min(res, j - i + 1)
                win_sum -= A[i]
                i += 1
        print(res)
        return -1 if res == float('inf') else res

solution = Solution()
solution.shortestSubarray([84, -37, 32, 40, 95], 167)
