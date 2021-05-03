"""
Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y),
then there exist integers a and b such that ax+by=g. In other words, there exists a linear combination of x and y equal to g.

Furthermore, g is the smallest positive integer that can be expressed in this form, i.e. g = min{ax+by | a, b in Z, ax+by > 0}.
"""
class Solution(object):
    def canMeasureWater_math(self, x, y, z):
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

    def canMeasureWater(self, x, y, z):
        if x + y < z:
            return False
        stack = [(0, 0)]
        visited = set(stack)
        while stack:
            new_stack = []
            for rx, ry in stack:
                if rx == z or ry == z or rx + ry == z:
                    return True
                # fill up x
                if (x, ry) not in visited:
                    visited.add((x, ry))
                    new_stack.append((x, ry))
                # full up y
                if (rx, y) not in visited:
                    visited.add((rx, y))
                    new_stack.append((rx, y))
                # empty x
                if (0, ry) not in visited:
                    visited.add((0, ry))
                    new_stack.append((0, ry))
                # empty y
                if (rx, 0) not in visited:
                    visited.add((rx, 0))
                    new_stack.append((rx, 0))
                # pour water from x to y till y is completely full or x is empty
                nx, ny = rx - min(rx, y - ry), ry + min(rx, y - ry)
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_stack.append((nx, ny))
                # pout water from y to x till x is completely full or y is empty
                nx, ny = rx + min(ry, x - rx), ry - min(ry, x - rx)
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_stack.append((nx, ny))
            stack = new_stack
            # print(stack)
        return False
