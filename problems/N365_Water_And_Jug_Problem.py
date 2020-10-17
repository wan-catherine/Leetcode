"""
Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y),
then there exist integers a and b such that ax+by=g. In other words, there exists a linear combination of x and y equal to g.

Furthermore, g is the smallest positive integer that can be expressed in this form, i.e. g = min{ax+by | a, b in Z, ax+by > 0}.
"""
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        def gcd(a, b):
            a, b = max(a, b), min(a, b)
            while b and a % b:
                a, b = b, a % b
            return b

        if z == 0:
            return True
        if (x == 0 and z != y) or (y == 0 and z != x):
            return False
        if (x == 0 and z == y) or (y == 0 and z == x):
            return True
        return z <= x + y and z % gcd(x, y) == 0