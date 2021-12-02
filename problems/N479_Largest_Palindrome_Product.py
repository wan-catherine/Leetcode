import math


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        low = pow(10, n-1)
        high = pow(10, n)
        def create_pali(num):
            rnum = 0
            cur = num
            count = 0
            while cur:
                rnum *= 10
                rnum += cur % 10
                cur //= 10
                count += 1
            return num * 10 ** count + rnum
        for i in range(high-1, low-1, -1):
            pali = create_pali(i)
            for d in range(high-1, int(math.sqrt(pali)), -1):
                if pali % d == 0 and pali / d >= low:
                    return pali % 1337
