class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        self.ans = 0
        def get(x):
            ans = x//seats
            if x%seats:
                ans += 1
            return ans

        n = len(roads) + 1

        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False]*n
        def dfs(node):
            if not visited[node]:
                visited[node] = True
                ans = 1
                for v in adj[node]:
                    temp = dfs(v)
                    self.ans += get(temp)
                    ans += temp
                return ans
            return 0
        dfs(0)
        return self.ans
