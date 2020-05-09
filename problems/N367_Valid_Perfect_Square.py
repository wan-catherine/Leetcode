class Solution:
    def isPerfectSquare_slow(self, num: int) -> bool:
        if num == 1:
            return True
        i = 2
        while i ** 2 < num:
            i += 1
        if i ** 2 != num:
            return False
        else:
            return True

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) //2
            mid_value = mid ** 2
            if mid_value == num:
                return True
            if mid_value < num:
                left = mid + 1
            else:
                right = mid -1
        return False
