class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        cnt = 0
        if cnt == n:
            return True
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                i += 2
                cnt += 1
                if cnt == n:
                    return True
            else:
                i += 1
        return False
