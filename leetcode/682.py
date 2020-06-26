class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        total = 0
        for op in ops:
            if op == "C":
                total -= scores[-1]
                del scores[-1]
            elif op == "D":
                cur = (scores[-1] * 2)
                total += cur
                scores.append(cur)
            elif op == "+":
                cur = (scores[-1] + scores[-2])
                total += cur
                scores.append(cur)
            else:
                cur = int(op)
                total += cur
                scores.append(cur)
        return total
