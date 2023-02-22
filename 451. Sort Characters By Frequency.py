class Solution:
    def frequencySort(self, s: str) -> str:
        def zero():
            return 0
        d = collections.defaultdict(zero)
        for i in s:
            d[i]+=1
        temp = list(d.items())
        temp.sort(key=lambda x:x[1], reverse=True)
        ans = []
        for ch, n in temp:
            ans.append(ch*n)
        return ''.join(ans)
