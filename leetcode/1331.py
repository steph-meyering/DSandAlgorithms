class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        a = sorted(enumerate(arr), key=lambda x: x[1])
        rank = 1
        prev = a[0][1]
        for i, n in a:
            if n > prev:
                rank += 1
                prev = n
            arr[i] = rank
        return arr
