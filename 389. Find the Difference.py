class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        ans = 0
        for i in s+t:
            ans = ans^ord(i)
        return chr(ans)
