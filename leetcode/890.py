class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            d = {}
            seen = set()
            for i, char in enumerate(pattern):
                if char not in d:
                    d[char] = word[i]
                    if word[i] not in seen:
                        seen.add(word[i])
                    else:
                        break
                elif d[char] != word[i]:
                    break
                if i == len(pattern) - 1:
                    res.append(word)
        return res
