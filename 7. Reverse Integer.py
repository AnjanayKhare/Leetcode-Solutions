def leng(n):
    if n<0:
        n = abs(n)
    ans = 0
    while n:
        ans +=1
        n = n//10
    return ans

class Solution:
    def reverse(self, x: int) -> int:
        tt = 1
        if x<0:
            tt = -1
        ans = 0
        x = abs(x)
        t = leng(x)
        i = 0
        while t:
            t-=1
            temp = x//int(10**t)
            x = x%int(10**t)
            ans += temp*int(10**i)
            i+=1
        up = (2**31) - 1
        down = -1*(up+1)
        ans = ans*tt
        if down<= ans <= up:
            return ans
        return 0
