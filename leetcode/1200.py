class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        dif = float("inf")
        res = []
        for i in range(1, len(arr)):
            a = sorted_arr[i-1]
            b = sorted_arr[i]
            cur_dif = b - a
            if cur_dif < dif:
                dif = cur_dif
                res = [[a, b]]
            elif cur_dif == dif:
                res.append([a, b])
        return res
