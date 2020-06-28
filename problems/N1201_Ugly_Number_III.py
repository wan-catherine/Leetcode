class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        self.ab = self.get_least_common_multiple(a, b)
        self.ac = self.get_least_common_multiple(a, c)
        self.bc = self.get_least_common_multiple(b, c)
        self.abc = self.get_least_common_multiple(self.ab, c)

        left, right = 1, 10**18+1
        while left < right:
            mid = (right - left) // 2 + left
            count = self.count_ugly_number_for(mid, a, b, c)
            if count < n:
                left = mid + 1
            else:
                right = mid
        return left

    def count_ugly_number_for(self, num, a, b, c):
        return num // a + num // b + num // c - num // self.ab - num // self.ac - num // self.bc + num // self.abc

    def get_gcd(self, a, b):
        if a > b :
            x, y = a, b
        else:
            x, y = b, a

        while y:
            x, y = y, x%y
        return x

    def get_least_common_multiple(self, a, b):
        return a*b // self.get_gcd(a, b)

