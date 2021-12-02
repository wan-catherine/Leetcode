"""
Key point : how to create palindrome num.
we can know for num : xyz, there are two ways to create a palindrome number from it:
    1. xyz ==> xyzyz
    2. xyz ==> xyzzyx

so we can start from the length = 1 and loop all numbers then create palindrome numbers.
xyz -> calculate to get zyx
then xyz * 10 ** 3 + zyx  ==> xyzzyx
xyz // 10 * 10 ** 3 + zyx  ==> xyzyx
"""

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        res = 0
        count = 0
        l = 1
        def get_pali(num, flag):
            rnum = 0
            cur = num
            c = 0
            while cur:
                v = cur % 10
                rnum *= 10
                rnum += v
                cur //= 10
                c += 1
            if flag:
                num //= 10
            return num * (10 ** c) + rnum

        def check(num):
            # this way will be TLE
            # n, rn, c = 0, 0, 0
            # while num:
            #     v = num % k
            #     n += v * (k ** c)
            #     rn *= k
            #     rn += v
            #     num //= k
            #     c += 1
            # return n == rn

            arr = []
            while num:
                v = num % k
                arr.append(v)
                num //= k
            return arr[::-1] == arr

        while True:
            for num in range(10**(l-1), 10**l):
                val = get_pali(num, 1)
                if check(val):
                    count += 1
                    res += val
                    if count == n:
                        return res
            for num in range(10**(l-1), 10**l):
                val = get_pali(num, 0)
                if check(val):
                    count += 1
                    res += val
                    if count == n:
                        return res
            l += 1