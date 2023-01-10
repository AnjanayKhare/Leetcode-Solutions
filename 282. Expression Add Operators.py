class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # l = list(map(int, num))
        n = len(num)
        self.ans = []
        def trev(curr, i):
            if i == n:
                if eval(curr) == target:
                    self.ans.append(curr)
                return
            if i==0:
                for j in range(1, n+1):
                    trev(num[i:j], j)
                    if num[i] == '0':
                        return
                return
            for j in range(i+1, n+1):
                trev(curr + '+' + num[i:j], j)
                trev(curr + '-' + num[i:j], j)
                trev(curr + '*' + num[i:j], j)
                if num[i] == '0':
                    return
        trev('', 0)
        return self.ans
