"""
Notice here one and two can be zero.
So we can't use 'not one/two' to check if it's None
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = None, None
        for i in nums:
            if one == None:
                one = i
                continue

            if two != None and i > two:
                return True

            if one != None and i > one:
                two = i if two == None else min(i, two)
                continue
            if one > i:
                one = i
        return False

