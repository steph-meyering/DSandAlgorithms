from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = Counter(s)
        # for c in s:
        #     if c not in freq:
        #         freq[c] = 0
        #     freq[c] += 1
        for c in t:
            if c not in freq:
                return False
            else:
                freq[c] -= 1
                if freq[c] == 0:
                    del freq[c]
        return not freq
