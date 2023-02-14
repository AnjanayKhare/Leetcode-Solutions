class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=='0':
            return b
        if b=='0':
            return a
        
        ans = []
        a = a[::-1]
        b = b[::-1]

        rem = '0'
        for i in range(max(len(a), len(b))):
            temp1 = '0'
            temp2 = '0'
            if len(b)>i:
                temp1 = b[i]
            if len(a)>i:
                temp2 = a[i]
            if temp1 == temp2 == '0':
                ans.append(rem)
                rem = '0'
            elif temp1 == temp2 == '1':
                ans.append(rem)
                rem = '1'
            else:
                if rem=='1':

                    ans.append('0')
                    rem = '1'
                else:
                    ans.append('1')
                    rem = '0'
        if rem=='1':
            ans.append('1')
        return ''.join(ans[::-1])
