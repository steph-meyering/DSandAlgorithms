class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0
        res = len(s)
        smap = Counter(s)
        for c in t:
            if c in smap and smap[c] > 0:
                smap[c] -= 1
                res -= 1
        return res
