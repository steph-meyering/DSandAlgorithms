class Solution:
    def validPalindrome(self, s: str, d = 1) -> bool:
        i, j = 0, len(s) -1
        while i < j:
            if s[i] != s[j]:
                if d > 0:
                    return self.validPalindrome(s[i+1:j+1], 0) or self.validPalindrome(s[i:j], 0)
                else:
                    return False
            i += 1
            j -= 1
        return True
