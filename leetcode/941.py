class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        up = False
        down = False
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            if not up:
                up = True
            i += 1
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            if not down:
                down = True
            i += 1

        return up and down and i == len(arr) - 1
