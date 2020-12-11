class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        s, e = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= e:
                e = max(e, cur[1])
            else:
                res.append([s, e])
                s, e = cur[0], cur[1]
        res.append([s, e])
        return res
