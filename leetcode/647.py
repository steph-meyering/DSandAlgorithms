class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = []
        for i in range(n):
            dp.append([0] * n)
        for i in reversed(range(n)):
            for j in range(i, n):
                if i == j or (j - i == 1 and s[j] == s[i]) or (dp[i+1][j-1] == 1 and s[j] == s[i]):
                    dp[i][j] = 1
                    count += 1
        return count
    # explanation:
    # https://leetcode.com/problems/palindromic-substrings/discuss/589576/javascript-DP-w-comments-and-explanation
