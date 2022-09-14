import sys


class SegTreePoint:
    def __init__(self, start, end, status, left=None, right=None):
        self.start = start
        self.end = end
        self.status = status   # largest value in [start, end]
        self.left = left
        self.right = right

    def buildTree(self, s, e, v):
        if s == e:
            self.start, self.end = s, e
            self.status = v
            return
        mid = (s + e) // 2
        if not self.left:
            self.left = SegTreePoint(s, mid, v)
            self.left.buildTree(s, mid, v)
            self.right = SegTreePoint(mid+1, e, v)
            self.right.buildTree(mid+1, e, v)
            self.status = max(self.left.status, self.right.status)

    def updateRange(self, s, e, v):
        if e < self.start or s > self.end:
            return
        if s <= self.start and e >= self.end:
            self.status = v
            return
        if self.left:
            self.left.updateRange(s, e, v)
            self.right.updateRange(s, e, v)
            self.status = max(self.left.status, self.right.status)

    def queryRange(self, s, e):
        if e < self.start or s > self.end:
            return -sys.maxsize
        if s <= self.start and e >= self.end:
            return self.status
        if self.left:
            res = max(self.left.queryRange(s, e), self.right.queryRange(s, e))
            return res
        return self.status

class SegTreeArray():
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * n

    # this is [l, r) which include l but not include r.
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            nval = max(self.tree[i * 2], self.tree[i * 2 + 1])
            if self.tree[i] == nval:
                return
            self.tree[i] = nval

