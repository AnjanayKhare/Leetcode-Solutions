class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)
        @cache
        def get(i, m, p):
            if i==n:
                return 0
            if p:
                score = 0
                temp = 0
                for x in range(2*m):
                    if x+i<n:
                        temp += piles[x+i]
                        score = max(score, get(x+i+1, max(m, x+1), p^1) + temp)
                    else:
                        break
            else:
                score = 1000000
                temp = 0
                for x in range(2*m):
                    if x+i<n:
                        score = min(score, get(x+i+1, max(m, x+1), p^1))
                    else:
                        break
            return score
        
        return get(0, 1, 1)
