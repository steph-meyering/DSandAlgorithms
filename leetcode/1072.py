class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        h = {}
        max_rows = 0
        for r in matrix:
            sequence = ""
            cur_streak = 1
            last_seen = r[0]
            for i in range(1, len(r)):
                if r[i] == last_seen:
                    cur_streak += 1
                else:
                    sequence += str(cur_streak)
                    cur_streak = 1
            if sequence not in h:
                h[sequence] = 0
            h[sequence] += 1
            max_rows = max(max_rows, h[sequence])
        return max_rows
