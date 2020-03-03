"""
In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
"""
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) < 2:
            return barcodes
        n = len(barcodes)
        ans = [0] * len(barcodes)
        q = {}
        for i in barcodes:
            if i in q:
                q[i] = q.get(i) + 1
            else:
                q[i] = 1

        q = dict(sorted(q.items(), key=lambda x: x[1], reverse=True))
        i1 = 0
        for i, j in q.items():
            for _ in range(j):
                ans[i1] = i
                i1 = i1 + 2
                if i1 >= n:
                    i1 = 1

        return ans



