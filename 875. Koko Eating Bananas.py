class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        ans = max(piles)*n
        hSpeed = ans
        lSpeed = 1
        def get(speed):
            ans = 0
            for i in piles:
                ans += int(ceil(i/speed))
            return ans
        
        while lSpeed<=hSpeed:
            speed = (lSpeed+hSpeed)//2
            time = get(speed)
            if time > h:
                lSpeed = speed+1
            else:
                hSpeed = speed-1
                ans = min(ans, speed)
        return ans
