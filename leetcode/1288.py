class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        sorted_pairs = sorted(intervals, key=lambda e: (e[0], -e[1]))
        count = 0
        max_end = 0
        for pair in sorted_pairs:
            start = pair[0]
            end = pair[1]
            if end > max_end:
                count += 1
                max_end = end
        return count
