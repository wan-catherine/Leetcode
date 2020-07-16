class Solution(object):
    def myPow_linear_slow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        flag = True if n >= 0 else False
        n = abs(n)
        res = 1
        while n > 0 :
            res *= x
            n -= 1

        if flag:
            return res
        else:
            return 1/res

    # x ** n == x ** (n // 2) * x ** (n // 2)  for n is even
    # x ** n == x ** (n // 2) * x ** (n // 2) * x  for n is odd
    def myPow_binary(self, x, n):
        if n == 0:
            return  1
        if n > 0:
            return self.pow_recursion(x, n)
        if n < 0:
            return 1/ self.pow_recursion(x, -n)

    def pow_recursion(self, x, n):
        if n == 0:
            return 1

        temp = self.pow_recursion(x, n // 2)
        if n % 2 == 0:
            return temp * temp
        else:
            return temp * temp * x

    """
    First : change n into binary  p = 2 ** 10  n = 10 (1010)  ==> p = 2 ** (1*2**3 + 0*2**2 + 1*2**1 + 0*2**0)
    The key point is : x ** (2 ** y) = [x ** (2 ** (y-1))] * [x ** (2 ** (y-1))]
    """
    def myPow(self, x, n):
        if n == 0:
            return  1
        if n > 0:
            return self.pow_other_way(x, n)
        if n < 0:
            return 1/ self.pow_other_way(x, -n)

    def pow_other_way(self, x, n):
        res = 1
        while n > 0:
            if n & 1 :
                res *= x
            x *= x  #key point
            n = n >> 1
        return res