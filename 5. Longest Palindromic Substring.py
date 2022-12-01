import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        x = 0
        y = 0
        for i in range(n) :
            dp[i][i] = 1
            if i + 1 < n :
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = 1
                    x = i
                    y = i+1
        for leng in range(2, n):
            i = 0
            j = leng
            while j < n:
                if (s[i] == s[j]) and dp[i + 1][j - 1] :
                    dp[i][j] = 1
                    x = i
                    y = j
                i += 1
                j += 1
        return s[x :y + 1]
