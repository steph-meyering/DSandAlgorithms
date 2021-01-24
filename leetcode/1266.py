class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)-1):
            A = points[i]
            B = points[i+1]
            res += self.shortestFromAtoB(A, B)
        return res

    def shortestFromAtoB(self, A, B):
        x1, y1 = A
        x2, y2 = B
        return max(abs(x1-x2), abs(y1-y2))
