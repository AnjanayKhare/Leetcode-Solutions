class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        par = [[] for i in range(n)]
        rank = [[1]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                par[i].append((i, j))
        

        def find(i, j):
            if par[i][j] == (i, j):
                return (i, j)
            p = find(*par[i][j])
            par[i][j] = p
            return p
        
        def union(i, j, x, y):
            pi, pj = find(i, j)
            px, py = find(x, y)
            if pi==px and pj==py:
                return
            if rank[pi][pj] < rank[px][py]:
                pi, px = px, pi
                pj, py = py, pj
            
            par[px][py] = (pi, pj)
            rank[pi][pj] += rank[px][py]

        def isValid(x, y):
            return 0<=x<n and 0<=y<m
        
        d = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for x in range(n):
                        if grid[x][j]:
                            union(x, j, i, j)
                    for y in range(m):
                        if grid[i][y]:
                            union(i, y, i, j)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if par[i][j] == (i, j) and rank[i][j] > 1:
                    ans += rank[i][j]
        
        return ans
