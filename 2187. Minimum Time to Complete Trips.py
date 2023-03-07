class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        l = 1
        h = time[-1]*totalTrips

        def getBus(t):
            ans = 0
            for i in time:
                ans += mid//i
            return ans
        ans = h
        while l<=h:
            mid = (l+h)//2
            trips = getBus(mid)
            if trips < totalTrips:
                l=mid+1
            else:
                ans = min(ans, mid)
                h=mid-1
        return ans
