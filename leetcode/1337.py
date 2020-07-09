from collections import deque
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h = {}
        for i in range(len(mat)):
            num_ones = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    num_ones += 1
            if num_ones not in h:
                h[num_ones] = deque()
            h[num_ones].append(i)
        res = []
        i = 0
        while len(res) < k:
            if i in h and len(h[i]) > 0:
                res.append(h[i].popleft())
            else:
                i += 1
        return res