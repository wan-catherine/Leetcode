import math


class Solution:
    def primePalindrome_before(self, n: int) -> int:
        length = len(str(n))

        def is_prime(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        def create(l, cur):
            if l == 0:
                temp = ''.join(cur + cur[::-1])
                return [int(temp)]
            if l == 1:
                ans = []
                if cur:
                    for i in range(10):
                        temp = ''.join(cur + [str(i)] + cur[::-1])
                        ans.append(int(temp))
                else:
                    ans = [2, 3, 5, 7]
                return ans
            res = []
            if not cur:
                for i in '13579':
                    cur.append(i)
                    res.extend(create(l - 2, cur))
                    cur.pop()
            if cur:
                for i in range(10):
                    cur.append(str(i))
                    res.extend(create(l - 2, cur))
                    cur.pop()
            return res

        while True:
            nums = create(length, [])
            nums.sort()
            if n <= nums[-1]:
                for num in nums:
                    if num < n:
                        continue
                    if is_prime(num):
                        return num
            length += 1

    """
    Update at 20211202
    Key point : xyzzyx will not be prime, because it can be divided by 11, except 11 itself.
    So we need to deal with the special situation when n <= 11. 
    
    Then for all other palindrome, we can only consider xyz ==> xyzyx. 
    
    """
    def primePalindrome(self, n: int) -> int:
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11
        ns = str(n)
        ln = len(ns)

        def check(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        num = 10 ** (ln // 2)
        while True:
            half = str(num)
            val = int(half + half[:-1][::-1])

            # print(val)
            if val >= n and check(val):
                return val
            num += 1


