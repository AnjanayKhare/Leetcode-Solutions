class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp1 = [-inf]*n
        dp2 = [inf]*n

        dp1[0] = prices[0]
        dp2[-1] = prices[-1]
        for i in range(1, n):
            j = n-i-1
            dp1[i] = min(dp1[i-1], prices[i])
            dp2[j] = max(dp2[j+1], prices[j])
        ans = 0
        for i, j in zip(dp1, dp2):
            ans = max(ans, j-i)
        return ans
