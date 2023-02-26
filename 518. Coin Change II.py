class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins.sort()
        n = len(coins) + 1
        dp = [[0]*(amount+1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            c = coins[i-1]
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j-c>=0:
                    dp[i][j] += dp[i][j-c]
        return dp[-1][-1]
