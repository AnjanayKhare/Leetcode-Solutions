class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        h = (len(nums)-1)//2 - 1
        while l<=h:
            mid = (l+h)//2
            if nums[mid*2]!=nums[mid*2 + 1]:
                if not ((mid*2 -1>=0 and nums[mid*2] == nums[mid*2-1]) or (mid*2 + 1<len(nums) and nums[mid*2] == nums[mid*2 +1])):
                    return nums[mid*2]

                h = mid-1
            else:
                l = mid+1
        print(mid)
        if not ((mid*2 -1>=0 and nums[mid*2] == nums[mid*2-1]) or (mid*2 + 1<len(nums) and nums[mid*2] == nums[mid*2 +1])):
            return nums[mid*2]

        return nums[mid*2 + 2]
