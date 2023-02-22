class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1 = m2 = m3 = -100000000000
        m1 = max(nums)
        for n in nums:
            if n<m1:
                m2 = max(m2, n)
        for n in nums:
            if n<m2:
                m3 = max(m3, n)

        if m3==-100000000000:
            return m1
        return m3
