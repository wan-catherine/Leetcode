"""
Majority Voting Algorithm , Boyer-Moore Algorith
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        bench = length // 3
        candidate = 0
        count = 0
        for i in nums:
            if count > bench:
                break
            if count == 0:
                candidate = i
            if i == candidate:
                count += 1
            else:
                count -= 1
        candidate_1 = candidate + 1
        count = 0
        for i in nums:
            if i == candidate:
                continue
            if count == 0:
                candidate_1 = i
            if i == candidate_1:
                count += 1
            else:
                count -= 1


        count, count_1 = 0,0
        for i in nums:
            if i == candidate:
                count += 1
            elif i == candidate_1:
                count_1 += 1

        res = []
        if count > len(nums) // 3:
            res.append(candidate)
        if count_1 > len(nums) // 3:
            res.append(candidate_1)
        return res