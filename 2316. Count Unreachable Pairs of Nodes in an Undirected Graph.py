class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        par = [i for i in range(n)]
        rank = [1]*n


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
                if rank[p1]<rank[p2]:
                    p1, p2 = p2, p1
                
                par[p2] = p1
                rank[p1] += rank[p2]
        
        for u, v in edges:
            union(u, v)
        ans = 0
        conn = 0

        for i in range(n):
            if par[i] == i:
                ans += conn*rank[i]
                conn += rank[i]
        
        return ans
