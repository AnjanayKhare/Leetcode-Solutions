class Solution:
    def convertToTitle(self, n: int) -> str:
        t = 26
        arr = []
        temp = 0
        l = 0
        while temp<n:
            temp += t
            l+=1
            t*=26
        
        for i in range(l-1, -1, -1):
            ans = 0
            temp = int(26**(i))
            while ans*temp < n:
                ans += 1
            arr.append(chr(ord("A") + ans - 2))
            n-= temp*(ans-1)
        
        arr[-1] = chr(ord(arr[-1]) + 1)
        return ''.join(arr)
