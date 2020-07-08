class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 2:
            return True
        j = 0
        while A[j] == A[j+1] and j < len(A) - 2:
            j += 1
        if j == len(A) - 2:  # array is comprised of only same nums
            return True
        if A[j] < A[j+1]:  # array should be increasing
            for i in range(j, len(A)-1):
                if A[i] > A[i+1]:
                    return False
            return True
        else:  # array should be decreasing
            for i in range(j, len(A)-1):
                if A[i] < A[i+1]:
                    return False
            return True
