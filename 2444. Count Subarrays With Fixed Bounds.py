class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        

        ind1 = -1
        ind2 = -1
        bad  = -1
        ans = 0
        for i, n in enumerate(nums):
            if not minK<=n<=maxK:
                bad = i
            if minK==n:
                ind1 = i
            if maxK==n:
                ind2 = i
            
            start = min(ind1, ind2)
            if start>bad:
                ans += start - bad
        return ans
