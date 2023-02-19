from sortedcontainers import SortedList, SortedSet, SortedDict

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x:x[1], reverse=True)
        n = len(boxTypes)
        ans = 0
        for i in range(n):
            if truckSize==0:
                break
            total = boxTypes[i][0]*boxTypes[i][1]
            if truckSize>=boxTypes[i][0]:
                ans += total
                truckSize -= boxTypes[i][0]
            else:
                ans += truckSize*boxTypes[i][1]
                truckSize = 0
        return ans
