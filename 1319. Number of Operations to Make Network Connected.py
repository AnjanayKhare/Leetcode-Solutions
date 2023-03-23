class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

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
                rank[p1]+=rank[p2]
            
        
        if len(connections) < n-1:
            return -1
        
        for i, j in connections:
            union(i, j)
        ans = 0
        for i in range(n):
            if par[i] == i:
                ans +=1
        
        return ans-1
