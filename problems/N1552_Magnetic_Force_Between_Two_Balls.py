class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        self.length = len(position)
        self.positions = position
        res = 1
        left, right = 1, position[-1] - position[0] + 1
        while left < right:
            mid = (right - left) // 2 + left
            if self.count(mid) >= m:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid
        return res

    def count(self, target):
        num = 1
        cur = 0
        for i in range(1, self.length):
            if self.positions[i] - self.positions[cur] >= target:
                num += 1
                cur = i
        return num
