class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0 for _ in range(len(boxes))]
        ball_indices = [i for i, char in enumerate(boxes) if char == "1"]
        for i in range(len(boxes)):
            for ball_i in ball_indices:
                res[i] += abs(ball_i - i)
        return res