"""
This is a difficult problem.
we need to divide into three sub problems.

first : find i numbers which is the largest number by keeping the order
second : find k - i numbers which is the largest number by keeping the order
third : merge first and second , then return the largest one

first and third , we can use monotonic stack to get the answer .
merge part is different from "merge sort" , see test_maxNumber_1
[6,7], [6,0,4]
when use merge sort directly , it possible to get [6,6,7,0,4]
but here we need to always use the largest digit from those two array .
so use compare .
"""
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        num1_len = len(nums1)
        num2_len = len(nums2)
        res = 0
        for i in range(k+1):
            if i <= num1_len and k-i <= num2_len:
                res1 = self.get_max_number_from(nums1, i)
                res2 = self.get_max_number_from(nums2, k - i)
                res = max(res, self.merge(res1, res2))
        return [int(x) for x in str(res)]


    def get_max_number_from(self, nums, k):
        nums_len = len(nums)
        if k >= nums_len:
            return nums[:]
        discard = nums_len - k
        stack = []
        for i in nums:
            while stack and stack[-1] < i and discard > 0:
                stack.pop()
                discard -= 1
            stack.append(i)
        return stack[:k]

    def merge_slow(self, num1, num2):
        res = []
        while num1 or num2:
            if num1 > num2:
                res.append(num1[0])
                num1 = num1[1:]
            else:
                res.append(num2[0])
                num2 = num2[1:]
        return 0 if not res else int(''.join([str(x) for x in res]))

    # concise and fast
    # from this I know that we can directly compare two list!
    def merge(self, num1, num2):
        res = [max(num1, num2).pop(0) for _ in num1 + num2]
        return 0 if not res else int(''.join([str(x) for x in res]))