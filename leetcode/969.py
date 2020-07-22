class Solution:
    def flip(self, A, k):
        i, j = 0, k-1
        while i < j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    
    def pancakeSort(self, A: List[int]) -> List[int]:
        last_element = len(A) #3
        res = [] #[7,]
        while last_element > 1:
            i = A.index(last_element)
            if i == last_element - 1:
                last_element -= 1
                continue
            if i != 0:
                self.flip(A,i+1)
                res.append(i + 1)
            self.flip(A, last_element)
            res.append(len(A[:last_element]))
            last_element -= 1
        return res
                
        