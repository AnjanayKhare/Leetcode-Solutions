from collections import defaultdict

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        similar = defaultdict(set)
        n = len(arr)
        for i in range(n):
            similar[arr[i]].add(i)
        q = deque([0])
        

        dist = [-1]*n
        dist[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            if u+1<n and dist[u+1]<0:
                dist[u+1] = dist[u]+1
                q.append(u+1)
                if u+1==n-1:
                    return dist[u+1]
            if u-1>-1 and dist[u-1] < 0:
                q.append(u-1)
                dist[u-1] = dist[u]+1
            for i in similar[arr[u]]:
                if dist[i]<0:
                    q.append(i)
                    dist[i] = dist[u]+1
                    if i==n-1:
                        return dist[n-1]
            del similar[arr[u]]
        return dist[-1]
                
