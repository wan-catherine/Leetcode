"""
s(i+2) = s(i) + 1 + r(i(s(i)) +   1   + s(i) + 0 + r(i(s(i))

So use binary search :
    if move to left , then mid is 1
    if move to right, then mid is 0

But we need to conside some special cases :
    1. when there are [0, 1, 1] => right - left == 3,
            then move to left , mid is 0
            move to right, mid i s 1
    2. when n= 1, k = 1, the very first is 0. So here we can use :
            if k == 1, then return 0
"""
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1:
            return "0"
        num = 1
        while n > 1:
            num = 2 * num + 1
            n -= 1
        # print(num)
        left, right = 1, num+1
        flag = True
        while left < right:
            mid = (right - left) // 2 + left
            if mid == k:
                return "1" if flag == True else "0"
            elif mid > k:
                flag = True if right - left > 2 else False
                if right - left == 3:
                    flag = not flag
                right = mid
            else:
                flag = False if right - left > 2 else True
                if right - left == 3:
                    flag = not flag
                left = mid + 1