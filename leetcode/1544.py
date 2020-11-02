class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if stack and stack[-1].casefold() == char.casefold() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
