"""
https://leetcode.com/problems/mirror-reflection/discuss/146336/Java-solution-with-an-easy-to-understand-explanation
When there is odd times of reflection, it will be left : 2.
when there is even times of reflection, it will be right : 0 or 1.
So we need to consider how many rooms. if even number rooms, then it will be 0, or it will be 1.

"""
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        rooms, reflections = 1, 1
        while p * rooms != reflections * q:
            # here we increase reflections first, because reflections might be more than rooms.
            reflections += 1
            rooms = reflections * q // p

        m, n = rooms % 2, reflections % 2
        if not n:
            return 2
        if m:
            return 1
        else:
            return 0
        return -1
