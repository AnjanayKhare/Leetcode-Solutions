class Solution:
    def numberToWords(self, n: int) -> str:
        if n==0:
            return 'Zero'
        tens = {
            0:'',
            1:'Ten',
            2:'Twenty',
            3:'Thirty',
            4:'Forty',
            5:'Fifty',
            6:'Sixty',
            7:'Seventy',
            8:'Eighty',
            9:'Ninety'
        }
        ones = {
            0:'',
            1:'One',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine'
        }
        ele = {
            10:'Ten',
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen'
        }
        def fun(n):
            if not n:
                return ''
            if n<10:
                return ones[n]
            elif n%10==0:
                return tens[n//10]
            elif 10<n<20:
                return ele[n]
            return f'{tens[(n%100)//10]} {ones[n%10]}'
        def word(n):
            if n==0:
                return ''
            if not n//100:
                return [fun(n)]
            if not n%100:
                return [f'{fun(n//100)} Hundred']
            return [f'{fun(n//100)} Hundred {fun(n%100)}']

        def word1(n):
            if n%100 == 0:
                ten = ''
            elif n<10:
                return [ones[n]]
            elif 11 <= n%100 <20:
                ten =  ele[n%100]
            elif (n%100)%10 == 0:
                ten = tens[(n%100)//10]
            else:
                ten = f'{tens[(n%100)//10]} {ones[n%10]}'
            if n//100 == 0:
                hundread = ''
            else:
                hundread = f"{ones[n//100]} Hundred"
            if not ten:
                return [hundread]
            elif not hundread:
                return [ten]
            return [hundread, ten]
        exp = {
            0:'',
            1:'Thousand',
            2:'Million',
            3:'Billion',
            4:'Trillion'
        }
        ans1 = deque(word(n%1000))
        ans = word(n%1000)
        for i in range(1, 4):
            n = n//1000
            if n%1000:
                # ans = word(n%1000) + ' ' + exp[i] + ' ' + ans
                temp = word(n%1000)[::-1]
                ans1.appendleft(exp[i])
                ans1.extendleft(temp)
                # ams1.append
        final = []
        for i in ans1:
            if i:
                final.append(i)
        # print(ans1)
        return ' '.join(final)
