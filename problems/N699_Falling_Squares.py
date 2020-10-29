import bisect


class Solution(object):
    def fallingSquares_(self, positions):
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
    def fallingSquares(self, positions):
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
