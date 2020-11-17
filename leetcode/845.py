class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i = 1
        up, down = 0, 0
        res = 0
        while i < len(A):
            if A[i-1] < A[i]:
                while i < len(A) and A[i-1] < A[i]:
                    i += 1
                    up += 1
                while i < len(A) and A[i-1] > A[i]:
                    i += 1
                    down += 1
                if down > 0:
                    res = max(res, up + down + 1)
                up, down = 0, 0
            else:
                i += 1
        return res
