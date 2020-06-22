class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        alpha = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if i != len(s) - 1 and alpha[s[i]] < alpha[s[i + 1]]:
                val += alpha[s[i + 1]] - alpha[s[i]]
                i += 2
            else:
                val += alpha[s[i]]
                i += 1
        return val
