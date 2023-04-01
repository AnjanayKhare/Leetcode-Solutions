class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = list(range(n))
        rank = [1]*n
        ac = [[accounts[i][0], set(accounts[i][1:])] for i in range(n)]
        def find(i):
            if par[i] == i:
                return i
            p = find(par[i])
            par[i] = p
            return p
        
        def union(i, j):
            p1 = find(i)
            p2 = find(j)

            if p1!=p2:
                if rank[p1] < rank[p1]:
                    p1, p2 = p2, p1
                par[p2] = p1
                rank[p1] += rank[p2]
        
        for i in range(n):
            for j in range(i+1, n):
                n1, s1 = ac[i]
                n2, s2 = ac[j]
                if s1.intersection(s2):
                    union(i, j)
        ans = [[accounts[i][0], set()] for i in range(n)]

        for i in range(n):
            p = find(i)
            ans[p][1] = ans[p][1].union(ac[i][1])
        final = []
        for i in range(n):
            if par[i] == i:
                final.append([ans[i][0], *sorted(ans[i][1])])
        return final
