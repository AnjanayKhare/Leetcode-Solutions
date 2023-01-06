class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def trev(i, j):
            if i>=len(s) and j>= len(p):
                return True
            if j>=len(p):
                return False
            match = (i< len(s)) and (s[i] == p[j] or p[j]=='.')
            if j+1<len(p) and p[j+1]=='*':
                return trev(i, j+2) or (match and trev(i+1, j))
            if match:
                return trev(i+1, j+1)
            return False
        return trev(0, 0)
