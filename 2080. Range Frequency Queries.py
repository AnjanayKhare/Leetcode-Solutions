from collections import defaultdict
def zero():
    return 0

class RangeFreqQuery:
    def __init__(self, arr: List[int]):

        self.n = len(arr)
        self.seg = [0]*(4*self.n)

        def build(l, h, node):
            if l==h:
                self.seg[node] = defaultdict(zero)
                self.seg[node][arr[l]] = 1
                return self.seg[node]
            mid = (l+h)//2
            left = build(l, mid, 2*node+1)
            right = build(mid+1, h, 2*node+2)
            res = defaultdict(zero)
            for i in left:
                res[i] += left[i]
            for i in right:
                res[i] += right[i]
            self.seg[node] = res
            return res
        
        build(0, self.n-1, 0)


    def query(self, left: int, right: int, value: int) -> int:
        self.ans = 0
        def qr(l, h, node):
            if left>h or right<l:
                return 0
            if left<=l and right>=h:
                return self.seg[node][value]
            
            mid = (l+h)//2

            lft = qr(l, mid, node*2+1)
            rght = qr(mid+1, h, node*2+2)
            return lft+rght
        
        return qr(0, self.n-1, 0)
