from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        helper = deque()
        count = 0
        for n in nums:
            if len(helper) == k:
                helper.popleft()
                if helper:
                    max_n = max(helper)
                    while True:
                        if helper[0] < max_n:
                            helper.popleft()
                        else:
                            break
            if not helper:
                helper.append(n)
            elif n >=helper[0]:
                helper.clear()
                helper.append(n)
            else:
                helper.append(n)
            count += 1
            if count >= k:
                res.append(helper[0])
        return res