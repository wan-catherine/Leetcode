import math


class Solution:
    def primePalindrome(self, n: int) -> int:
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





