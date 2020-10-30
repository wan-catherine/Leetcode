import bisect

"""
Key point : 
pos/height : show skyline. There is no intervals here!!!

the interval here is left close, right open : [l, l+s).
if start = 1, the side = 2, then [1,2] is the new one, it's not include 3: [1,3). 
So for the left point, we need to use : bisect.bisect/bisect.bisect_right to find the rightmost index. 
Because we need to after all possible point . so the hight of it should be height[i-1] . 
We can use both bisect.bisect or bisect.bisect_right, because , for pos , we can only have one duplicated pos. 

For the right point, because it's not included , so we need to find the leftmost index. we can know height[i:j] = [high, height[j-1]]. 
"""
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        height, pos, res = [0], [0], []
        cur = 0
        for l, s in positions:
            i = bisect.bisect(pos, l)
            j = bisect.bisect_left(pos, l+s)
            high = max(height[i-1:j] or [0]) + s
            pos[i:j] = [l, l + s]
            height[i:j] = [high, height[j-1]]
            cur = max(cur, high)
            res.append(cur)
        return res

    """
    brute force
    """
    def fallingSquares_bruteforce(self, positions):
        res = []
        intervals = []
        cur = 0
        for l, s in positions:
            start, end = l, l + s
            base = 0
            for i, j, h in intervals:
                # [start, end)
                if end <= i or start >= j:
                    continue
                base = max(base, h)
            height = base + s
            intervals.append((start, end, height))
            cur = max(cur, height)
            res.append(cur)
        return res

    def fallingSquares(self, positions):
        root = SegTree(0, 10**8+1, 0)
        res = []
        maximum = 0
        for l, s in positions:
            cur = root.get_status(l, l + s)
            maximum = max(maximum, cur + s)
            root.set_status(l, l+s, cur+s)
            res.append(maximum)
        return res

class SegTree:
    def __init__(self, start, end, status):
        self.start = start
        self.end = end
        self.status = status
        self.left, self.right = None, None

    def get_status(self, a, b):
        if a <= self.start and b >= self.end:
            return self.status
        if a >= self.end or b <= self.start:
            return 0
        if not self.left:
            return self.status
        l = self.left.get_status(a, b)
        r = self.right.get_status(a, b)
        return max(l, r)

    def set_status(self, a, b, s):
        if a <= self.start and b >= self.end:
            self.left, self.right = None, None
            self.status = s
            return
        if a >= self.end or b <= self.start:
            return
        if not self.left:
            mid = (self.end - self.start) // 2 + self.start
            self.left = SegTree(self.start, mid, self.status)
            self.right = SegTree(mid, self.end, self.status)
        self.left.set_status(a, b, s)
        self.right.set_status(a, b, s)
        self.status = max(self.left.status, self.right.status)



