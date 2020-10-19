class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i = 1
        j = 1
        while(j < len(arr)):
            if arr[i - 1] != arr[j]:
                arr[i] = arr[j]
                i += 1
            j += 1

        return i