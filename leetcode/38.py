class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ans = ""
        prev_ans = self.countAndSay(n - 1)
        prev_num = prev_ans[0]
        count = 1
        for i, n in enumerate(prev_ans):
            if i == 0:
                continue
            if prev_num == n:
                count += 1
            else:
                ans =  ans + f"{count}{prev_num}"
                count = 1
                prev_num = n
        ans = ans + f"{count}{prev_num}"
        return ans