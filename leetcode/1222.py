class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        directions = [[-1, 0],[-1, 1],[0, 1],[1, 1],[1, 0],[1, -1],[0, -1],[-1, -1]]
        positions = []
        for d in directions:
            new_pos = [d[0] + king[0], d[1] + king[1]]
            positions.append(new_pos)
        i = 0
        while i < 8:
            if positions[i][0] < 0 or positions[i][0] > 7 or positions[i][1] < 0 or positions[i][1] > 7:
                i += 1
            elif positions[i] in queens:
                res.append(positions[i])
                i += 1
            else:
                x, y = positions[i]
                a, b = directions[i]
                positions[i] = [x + a, y + b]
        return res