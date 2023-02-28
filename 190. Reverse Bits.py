class Solution:
    def reverseBits(self, n: int) -> int:
        def rev(c, n):
            if c==1:
                return n
            n1 = rev(c//2, n>>(c//2))
            n2 = rev(c//2, n&((1<<(c//2)) - 1))
            return n1| n2<<(c//2)
        return rev(32, n)
