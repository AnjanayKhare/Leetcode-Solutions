class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # if k==0:
        #     return num
        num2 = list(map(int, list(str(k))))
        if num==[0]:
            return num2
        ans = []
        num  =  num[::-1]
        num2 = num2[::-1]
        rem = 0
        for i in range(max(len(num), len(num2))):
            n1 = 0
            n2 = 0
            if i<len(num):
                n1 = num[i]
            if i<len(num2):
                n2 = num2[i]
            temp = (rem+n1+n2)%10
            ans.append(temp)
            rem = (rem+n1+n2)//10
        if rem:
            ans.append(rem)
        return ans[::-1]
