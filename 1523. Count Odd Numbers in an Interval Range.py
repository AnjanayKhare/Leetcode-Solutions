class Solution:
    def countOdds(self, low: int, high: int) -> int:
        high += 1
        le = high-low
        if le%2:
            if low%2:
                return ((high-low)//2)+1
            else:
                return (high-low)//2
        else:
            return (high-low)//2
