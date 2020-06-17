"""
To be a triangle, a,b,c should :
a+b>c and a+c>b and b+c>a
or
a-b<c and a-c<b and b-c<a

So first sort the nums by reverse order, then fix the first num as a .
we need to find two numbers (b and c) which b+c<a , then it will be a triangle.
Because a is the largest of (a,b,c).
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_len = len(nums)
        nums.sort(reverse=True)
        ans = 0
        for i in range(nums_len-2):
            left, right = i+1, nums_len-1
            while left < right:
                if nums[i] < nums[left] + nums[right]:
                    ans += right - left
                    left += 1
                else:
                    right -= 1
        return ans


