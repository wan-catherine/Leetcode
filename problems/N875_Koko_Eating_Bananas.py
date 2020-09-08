class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        length = len(piles)
        if length == H:
            return max(piles)
        right = max(piles)
        total = sum(piles)
        if total <= H:
            return 1
        left = total // H
        while left < right:
            mid = (right - left) // 2 + left
            if self.helper(mid, piles, H):
                right = mid
            else:
                left = mid + 1
        return left

    def helper(self, value, piles, H):
        hours = 0
        for pile in piles:
            if pile % value:
                hours += pile // value + 1
            else:
                hours += pile // value
        if hours > H:
            return False
        else:
            return True
