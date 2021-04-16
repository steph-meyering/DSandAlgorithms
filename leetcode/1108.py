class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub(r'\.','[.]', address)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return re.sub(r'\.','[.]', address)
        res = ""
        for char in address:
            if char == ".":
                res += '[.]'
            else:
                res += char
        return res