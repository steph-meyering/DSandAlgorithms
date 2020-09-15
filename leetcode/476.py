class Solution:
    def findComplement(self, num: int) -> int:
        bit_rep = bin(num)
        comp = ""
        for i, c in enumerate(bit_rep[2:]):
            comp += str((int(c) ^ 1))
        return int(comp, 2)
