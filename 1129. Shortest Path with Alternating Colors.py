class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red  = collections.defaultdict(list)
        blue = collections.defaultdict(list)
        
        for src, dest in redEdges:
            red[src].append(dest)
        for src, dest in blueEdges:
            blue[src].append(dest)
        answer = [-1]*n
        q = deque()
        q.append([0, 0, None])
        visit = set((0, None))
        while q:
            node, length, prev = q.pop()
            if answer[node] == -1:
                answer[node] = length
            # 0 -> red
            # 1 -> blue
            if prev!=0:
                for v in red[node]:
                    if (v, 0) not in visit:
                        visit.add((v, 0))
                        q.appendleft([v, length+1, 0])
            if prev!=1:
                for v in blue[node]:
                    if (v, 1) not in visit:
                        visit.add((v, 1))
                        q.appendleft([v, length+1, 1])
        
        return answer
