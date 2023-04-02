from bisect import *

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        

        # spells.sort()
        potions.sort()
        ans = []
        
        for i in spells:
            temp = bisect_left(potions, success/i)
            ans.append(len(potions) - temp)
        return ans
