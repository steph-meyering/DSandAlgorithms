class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        s = set()
        for p in [p1, p2, p3, p4]:
            s.add(str(p))
        if len(s) != 4:
            return False

        s1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        s2 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
        s3 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
        s4 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
        s5 = (p4[0] - p1[0]) ** 2 + (p4[1] - p1[1]) ** 2
        s6 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
        arr = [s1, s2, s3, s4, s5, s6]
        arr.sort()
        if arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
            return True
        return False
