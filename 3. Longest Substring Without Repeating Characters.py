class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        freq = [False for i in range(128)]
        n = len(s)
        ans = 0
        for i in range(n):
            temp = freq.copy()
            h = i
            while h<n:
                if temp[ord(s[h])]:
                    break
                temp[ord(s[h])] = True
                h+=1
            # print(temp, i)
            ans = max(ans, h-i)
        return ans
