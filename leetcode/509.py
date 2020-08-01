class Solution:

    def fib(self, N: int) -> int:
        memo = {0: 0, 1: 1}
        return self.fib_helper(N, memo)

    def fib_helper(self, N, memo):
        if N in memo:
            return memo[N]
        else:
            memo[N] = self.fib_helper(N - 1, memo) + \
                self.fib_helper(N - 2, memo)
            return memo[N]
