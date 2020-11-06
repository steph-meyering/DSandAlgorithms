class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, start, end = 0, 0, 1
        merged = []
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        m = newInterval
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            m[start] = min(m[start], intervals[i][start])
            m[end] = max(m[end], intervals[i][end])
            i += 1

        merged.append(m)

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
