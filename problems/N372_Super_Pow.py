"""
Goal = (a ^ exp) mod 1337
= a ^ ( exp mod φ(1337) ) mod 1337
= a ^ ( exp mod 1140) mod 1337
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a == 1:
            return 1
        if not a % 1337:
            return 0

        b = int(''.join(map(str, b))) % 1140
        return (a ** b) % 1337
