class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        count = Counter(stones)
        for jewel in jewels:
            if jewel in count:
                res += count[jewel]
        return res