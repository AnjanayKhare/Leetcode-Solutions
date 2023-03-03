class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def get(i, p):
            if i==n:
                return 0

            if p:
                score = -10000000
                temp = 0
                for j in range(i, min(i+3, n)):
                    temp+=stoneValue[j]
                    score = max(get(j+1, p^1)+temp, score)
                
            else:
                score = 1000000000
                for j in range(i, min(i+3, n)):
                    score = min(score, get(j+1, p^1))
            return score
        alice =  get(0, 1)
        bob = sum(stoneValue) - alice
        if alice>bob:
            return "Alice"
        elif bob>alice:
            return 'Bob'
        return "Tie"
