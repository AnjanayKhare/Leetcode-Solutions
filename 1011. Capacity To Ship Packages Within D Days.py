class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weights.sort()
        l = max(weights)
        h = sum(weights)
        n = len(weights)
        def getMin(x):
            temp = 0
            ans = 1
            for i in range(n):
                if temp+weights[i] > x:
                    temp = weights[i]
                    ans += 1
                else:
                    temp += weights[i]
            return ans
        ans = h
        while l<=h:
            mid = (l+h)//2
            temp = getMin(mid)
            if temp>days:
                l = mid+1
            else:
                ans = min(ans, mid)
                h = mid-1
        return ans
