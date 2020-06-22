class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        char_freq = {}
        for char in ransomNote:
            if char not in char_freq:
                char_freq[char] = 0
            char_freq[char] += 1
        for char in magazine:
            if char in char_freq:
                char_freq[char] -= 1
                if char_freq[char] == 0:
                    del char_freq[char]
                if char_freq == {}:
                    return True
        return False
