class Solution:
    def pivotInteger(self, n: int) -> int:
        temp = 1 + int(sqrt(1+2*(n*(n+1))) - 1)//2
        print(temp)
        if temp*(temp+1) != (n*(n+1))//2 +temp:
            return -1
        return temp
