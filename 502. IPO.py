class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        temp = [(i, j) for i, j in zip(profits, capital)]
        temp.sort(key=lambda x:x[1])
        i = 0
        heap = []
        for _ in range(k):
            while i<len(profits) and temp[i][1]<=w:
                heappush(heap, -1*temp[i][0])
                i+=1
            if heap:
                t = -1*heappop(heap)
                w+=t
        return w
