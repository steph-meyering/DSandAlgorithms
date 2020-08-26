class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while i < len(pushed):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
            i += 1
        return not bool(stack)
