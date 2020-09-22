"""
Majority Voting Algorithm , Boyer-Moore Algorith
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

20200922 update:
Here are two key points:
1. We need to count the two majority elements together!!!
        If check one by one, then if one less than 1/2, it will be wrong. test_majorityElement_4
2. We need to check i == candidate first , then check count == 0.
        If we check count == 0 first , then when one of the count becomes 0, it will renew the candidate. test_majorityElement_5

So we can think about it asks to find all elements that appear more than 1/4 times.
Then we need to consider three elements together !!!
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        candidate, candidate_1 = None, None
        count, count_1 = 0, 0
        for i in nums:
            if i == candidate:
                count += 1
            elif i == candidate_1:
                count_1 += 1
            elif count == 0:
                candidate = i
                count += 1
            elif count_1 == 0:
                candidate_1 = i
                count_1 += 1
            else:
                count -= 1
                count_1 -= 1
        count, count_1 = 0,0
        for i in nums:
            if i == candidate:
                count += 1
            elif i == candidate_1:
                count_1 += 1

        res = []
        if count > length // 3:
            res.append(candidate)
        if count_1 > length // 3:
            res.append(candidate_1)
        return res
