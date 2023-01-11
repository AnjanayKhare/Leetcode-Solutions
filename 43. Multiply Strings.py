class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        n = len(num1)
        m = 0
        arr = [[0]*i for i in range(n)]
        for i in range(n-1, -1, -1):
            last = 0
            temp1 = int(num1[i])
            for j in num2[::-1]:
                temp2 = int(j)
                dig = (temp1*temp2) + last
                arr[n-i-1].insert(0, dig%10)
                last = dig//10
            if last:
                arr[n-i-1].insert(0, last)
            m = max(m, len(arr[n-i-1]))
        for i in arr:
            while len(i)<m:
                i.insert(0, 0)
        ans = []
        rem = 0
        for i in range(m-1, -1, -1):
            temp = 0
            for j in range(n):
                temp += arr[j][i]
            temp += rem
            ans.insert(0, str(temp%10))
            rem = temp//10
        if rem:
            ans.insert(0, str(rem))
        return ''.join(ans)
