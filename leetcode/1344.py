class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour % 12)/12 * 360  # 105
        m = minutes/60 * 360  # 180
        h += minutes/60 * 360/12  # 15
        a = abs(h-m)
        return min(a, 360 - a)
