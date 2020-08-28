class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        self.flag = False
        self.helper(arr, start)
        return self.flag
        
    def helper(self, arr, start):
        if arr[start] == 0:
            self.flag = True
        if arr[start] > 0:
            val = arr[start]
            arr[start] = -arr[start]
            if start + val < len(arr):
                self.helper(arr, start + val)
            if start - val >= 0:
                self.helper(arr, start - val)