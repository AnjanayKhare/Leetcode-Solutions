class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        mx = sum(piles)

        @cache
        def trev(i, j, p):
            if j<i:
                return 0
            if i==j:
                if p:
                    return piles[i]
                return 0
            if p:
                return max(trev(i+1, j, p^1) + piles[i], trev(i, j-1, p^1) + piles[j])
            # eles:
            return min(trev(i+1, j, p^1), trev(i, j-1, p^1))
        
        mx_ans = trev(0, len(piles) - 1, 1)
        return mx_ans >= mx - mx_ans
