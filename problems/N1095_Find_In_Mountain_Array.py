import bisect


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        length = mountain_arr.length()
        left, right = 0, length
        # find the peak point
        while left < right:
            mid = (right - left) // 2 + left
            if mid >= 1 and mountain_arr.get(mid) > mountain_arr.get(mid - 1):
                left = mid + 1
            else:
                right = mid
        if left > 0 and mountain_arr.get(left) < mountain_arr.get(left - 1):
            left -= 1

        def binary_search(l, r, is_left):
            while l < r:
                mid = (r - l) // 2 + l
                val = mountain_arr.get(mid)
                if val == target:
                    return mid
                elif val < target:
                    if is_left:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    if is_left:
                        r = mid
                    else:
                        l = mid + 1
            if mountain_arr.get(left) == target:
                return left
            return -1
        # binary search for the left (increased half) and right (decreased half)
        res = binary_search(0, left, True)
        if res == -1:
            res = binary_search(left + 1, length, False)
        return res



