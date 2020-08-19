"""
[a,b,c,d,e,f,d]
a / (b,c,d,e,f,d) when numerator is fixed , we want denominator is as small as possible ,so the result will be maximum.
If we want (b,c,d,e,f,d) is the smallest one, then b/c/d/e/f/d will be the one (positive integers)
Then the result will be :
a/(b/c/d/e/f/d)
"""
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        length = len(nums)
        if length == 1:
            return str(nums[0])
        if length == 2:
            return f"{nums[0]}/{nums[1]}"

        res = str(nums[0]) + "/("
        for i in range(1, length):
            res += str(nums[i]) + '/'
        res = res[:-1] + ")"
        return res