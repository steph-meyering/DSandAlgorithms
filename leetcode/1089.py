class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        add = 0
        for i, num in enumerate(arr):
            if num == 0:
                add += 10
            arr[i] += add
        for i in range(len(arr) - 1, -1, -1):
            offset = arr[i] // 10
            val = arr[i] % 10
            new_i = i + offset
            if val == 0 and len(arr) >= new_i > 0:
                arr[new_i - 1] = 0
            if new_i < len(arr):
                arr[new_i] = val
