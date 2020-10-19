class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            for j in range(len(s), i-1, -1):
                if len(res) > j-i:
                    break
                sub = s[i:j]
                if sub == sub[::-1]:
                    if j-i > len(res):
                        res = sub
                        continue
        return res