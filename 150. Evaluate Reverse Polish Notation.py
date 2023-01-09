class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        n = len(tokens)
        def div(x, y):
            if x>=0 and y>=0:
                return x//y
            if abs(x)%abs(y) == 0:
                return x//y
            return (x//y) + 1
        opr = {
            '+' : lambda x, y: x+y,
            '-' : lambda x, y: x-y,
            '*' : lambda x, y: x*y,
            '/' : lambda x, y: x//y if x*y >=0 else div(x, y)
        }
        for i in range(n):
            temp = tokens[i]
            if temp in opr:
                y = q.pop()
                x = q.pop()
                z = opr[temp](x, y)
                q.append(z)
            else:
                q.append(int(temp))
        return q[-1]
