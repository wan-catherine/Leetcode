import math

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(num):
            side = int(math.sqrt(2*num))
            while side * (side + 1) > 2 *num:
                side -= 1

            diff = num - side * (side + 1) // 2
            arr = [i+1 for i in range(side)]
            for i in range(diff):
                arr[side-i-1] += 1

            level, ans = 0, 0
            for i in range(side):
                level += arr[i]
                ans += level
            return ans

        left, right = 1, 10**9+1
        while left < right:
            mid = (right - left) // 2 + left
            if check(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return left
