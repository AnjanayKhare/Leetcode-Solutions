class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        left = [0]*n
        right = [0]*n
        if nums[0]==1:
            left[0] = 1
        if nums[-1] == 1:
            right[-1] = 1
        for i in range(1, n):
            if nums[i]:
                left[i] = left[i-1] + 1
            j = n-i-1
            if nums[j]:
                right[j] = right[j+1] + 1
        ans = max(left[1], right[-2])
        for i in range(1, n-1):
            ans = max(ans, left[i-1]+right[i+1])
        return ans
