class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x1-x2) + abs(y1-y2)
                adj.append((i, j, d))
        
        adj.sort(key=lambda x:x[2])
        par = [i for i in range(n)]
        rank = [1]*n

        def find(i):
            if par[i]==i:
                return i
            
            p = find(par[i])
            par[i] = p
            return p
        
        def union(i, j):
            p1 = find(i)
            p2 = find(j)
            if p1 == p2:
                return False

            if rank[p1]<rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return True
        

        ans = 0
        for u, v, d in adj:
            if union(u, v):
                ans += d
        return ans
