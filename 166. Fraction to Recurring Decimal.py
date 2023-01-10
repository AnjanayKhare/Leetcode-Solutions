class Solution:
    def fractionToDecimal(self, a: int, b: int) -> str:
        if a%b == 0:
            return str(a//b)
        sign = -1 if a*b<0 else 1
        a = abs(a)
        b = abs(b)
        integer = a//b
        a = a%b
        r = {}
        fraction = []
        i = -1
        while a:
            i+=1
            # print(a, r)
            if a<b:
                # print("This")
                r[str(a)] = i
                a = a*10
                if i:
                    fraction.append('0')
                continue
            else:
                rem = str(a%b)
                fraction.append(str(a//b))
                a = (a%b)*10
                if rem in r:
                    # print(fraction)
                    ans = f'{integer}' '.' + ''.join(fraction[:r[rem]])+'(' + ''.join(fraction[r[rem]:]) + ')'
                    if sign==-1:
                        return '-'+ans
                    return ans
                    
                r[rem] = i
                # print(fraction)
        
        ans = f'{integer}' +'.'+ ''.join(fraction)
        if sign==-1:
            return '-'+ans
        return ans
