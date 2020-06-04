from collections import deque
"""
20200604

use a decreasing monotonic stack
but need to keep the length of stack is <= k

so after each time append a new number into the stack, 
we need to check:
first: if the current index is already >= k, 
if so , the stack[0] will be the k numbers largest one, add into res.

second: check the length of stack, if the current index - stack[0] >= k - 1, 
it means, for next loop , the stack[0] won't be in the k slide window,
so we need to pop it. 

"""
class Solution(object):
    def maxSlidingWindow_before(self, nums, k):
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

    # 20200604
    def maxSlidingWindow(self, nums, k):
        n_len = len(nums)
        # if n_len <= k:
        #     return [max(nums)]

        stack = []
        res = []
        for i in range(n_len):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            if i >= k - 1:
                res.append(nums[stack[0]])
            if i - stack[0] >= k -1:
                stack.pop(0)
        return res

