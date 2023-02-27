class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        k = log2(n)
        print(n)

        def trev(x1, y1, x2, y2):
            if x1==x2 and y1==y2:
                return Node(grid[x1][y1], 1, None, None, None, None)
            midx = (x1+x2)//2
            midy = (y1+y2)//2
            topLeft = trev(x1, y1, midx, midy)
            topRight = trev(x1, midy+1, midx, y2)
            bottomLeft = trev(midx+1, y1, x2, midy)
            bottomRight = trev(midx+1, midy+1, x2, y2)
            if (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) and (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf):
                return Node(topLeft.val, 1, None, None, None, None)
            return Node(1, 0, topLeft, topRight, bottomLeft, bottomRight)
        
        return trev(0, 0, len(grid)-1, len(grid)-1)
