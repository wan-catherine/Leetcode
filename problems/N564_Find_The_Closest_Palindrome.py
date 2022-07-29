import sys

"""
https://leetcode.com/problems/find-the-closest-palindrome/discuss/147949/Thinking-Process
the nearest palidrome only happens in root + each of [-1,0,1] (let's say the first half is root)

some corner cases : 
case 1. <= 10, OR equal to 100, 1000, 10000, ... We simply decrease n by 1.
case 2. 11, 101, 1001, 10001, 100001, ... We simply decrease n by 2.
case 3. 99, 999, 9999, 99999, ... We simply increase n by 2.
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        a = 10 ** (length - 1)
        if str(a) == n:
            return str(a - 1)
        if str(a + 1) == n:
            return str(a - 1)
        a *= 10
        if str(a - 1) == n:
            return str(a + 1)

        candidates = []
        root = int(n[:(length+1)//2])
        for i in [-1, 0, 1]:
            val = str(root + i)
            # here need to consider even or odd.
            if length % 2:
                num = int(val + val[:-1][::-1])
            else:
                num = int(val + val[::-1])
            candidates.append(num)
        diff = sys.maxsize
        val = int(n)
        res = None
        for n in candidates:
            # here need to remove n itself.
            if n == val:
                continue
            if diff > abs(val - n):
                res = n
                diff = abs(val - n)
            elif diff == abs(val - n):
                if n < res:
                    res = n
        return str(res)

    """
    https://github.com/wisdompeak/LeetCode/tree/master/String/564.Find-the-Closest-Palindrome
    """

    def nearestPalindromic_20220729(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        old = int(n)
        ni = '9' * (length - 1)
        oi = "1" + '0' * (length - 1) + "1"
        candidates = [ni, oi]
        if length % 2:
            half = int(n[:length // 2 + 1])
            shalf = str(half)
            plus = half + 1
            splus = str(plus)
            minor = half - 1
            sminor = str(minor)
            candidates.append(shalf + shalf[:-1][::-1])
            candidates.append(splus + splus[:-1][::-1])
            candidates.append(sminor + sminor[:-1][::-1])
        else:
            half = int(n[:length // 2])
            shalf = str(half)
            plus = str(half + 1)
            minor = str(half - 1)
            candidates.append(shalf + shalf[::-1])
            candidates.append(plus + plus[::-1])
            candidates.append(minor + minor[::-1])
        res = sys.maxsize
        for c in candidates:
            if c == n:
                continue
            ic = int(c)
            diff = abs(ic - old)
            if diff == abs(res - old):
                res = min(ic, res)
            elif diff < abs(res - old):
                res = ic
        return str(res)

