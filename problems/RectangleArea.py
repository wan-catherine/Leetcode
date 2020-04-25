class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        one = (A - C) * (B - D)
        two = (E - G) * (F - H)
        if one < 0:
            one *= -1
        if two < 0:
            two *= -1

        