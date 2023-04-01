class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def h_d(w1, w2):
            diff = 0
            for c1, c2 in zip(w1,w2):
                if c1 != c2: diff += 1
                if diff > 2: return False
            return True
        ds = [-1] * len(strs)
        def find(node):
            if ds[node] < 0: return node
            ds[node] = find(ds[node])
            return ds[node]
        for w1_idx, w1 in enumerate(strs):
            for w2_idx, w2 in enumerate(strs):
                if w1_idx != w2_idx:
                    p1, p2 = find(w1_idx), find(w2_idx)
                    if p1 != p2 and h_d(w1, w2):
                        if ds[p2] < ds[p1]: p1, p2 = p2, p1
                        ds[p1] += ds[p2]
                        ds[p2] = p1
        return sum(i < 0 for i in ds)
