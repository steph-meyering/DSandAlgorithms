class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        k = len(A) - 1
        res = []
        for num in A:
            res.append(0)
        while i <= j:
            if abs(A[i]) < abs(A[j]):
                res[k] = A[j] ** 2
                j -= 1
            else:
                res[k] = A[i] ** 2
                i += 1
            k -= 1
        return res
