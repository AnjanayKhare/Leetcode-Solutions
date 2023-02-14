class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [-1]*n
        stk = deque()

        for i in range(n):
            curr = prices[i]
            while stk and curr <= prices[stk[-1]]:
                j = stk.pop()
                ans[j] = curr
            stk.append(i)
        

        for i in range(n):
            if ans[i]==-1:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i]-ans[i]

        return ans
