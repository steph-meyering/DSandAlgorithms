class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res_len = max(len(a),len(b)) + 1
        res = ["0"] * res_len
        res = deque(res)
        rem = 0
        for i in range(1, res_len + 1):
            A = 0 if i > len(a) else int(a[-i])
            B = 0 if i > len(b) else int(b[-i])
            if (A + B + rem) % 2 == 1:
                res[-i] = "1"
            rem = (A + B + rem) // 2
        if res[0] == "0":
            res.popleft()
        return "".join(res)