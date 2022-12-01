class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = set(nums)
        for i in a:
            if (i in a) and (target-i in a):
                n1 = i
                n2 = target - i
                if n1==n2:
                    n = nums.count(n1)
                    if n>1:
                        an1 = nums.index(n1)
                        nums.remove(n1)
                        an2 = nums.index(n1) + 1
                        return [an1, an2]
                if n1!=n2:
                    return [nums.index(n1), nums.index(n2)]
