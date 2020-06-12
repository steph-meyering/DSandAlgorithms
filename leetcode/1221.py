class Solution:
    def balancedStringSplit(self, s: str) -> int:
        char_count = 0
        count = 0
        for i in range(len(s)):
            char_count = char_count + 1 if s[i] == "L" else char_count - 1
            if char_count == 0:
                count += 1 
        return count