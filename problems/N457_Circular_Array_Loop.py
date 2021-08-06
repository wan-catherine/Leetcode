"""
I read a lot of answers .
But still confused about how to decide to return True and how to end the loop.

We need to set nums[i] = 0 after we visit it.

"""
from typing import List


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        for index, value in enumerate(nums):
            if value == 0:
                continue
            current = index
            sign = value // abs(value)
            visited = set()
            while nums[current] * sign > 0:
                next = (nums[current] + current) % nums_len
                nums[current] = 0
                visited.add(current)
                if next in visited and current != next:
                    return True
                current = next
        return False

    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)
        # it works for both positive and negative index
        def next(cur):
            return (cur + nums[cur]) % length
        for i, n in enumerate(nums):
            if n == 0:
                continue
            slow, fast = i, i
            while True:
                if nums[next(fast)] * nums[i] < 0 or nums[next(next(fast))] * nums[i] < 0:
                    break
                fast = next(next(fast))
                slow = next(slow)
                if slow == fast:
                    if slow != next(slow):
                        return True
                    break
            # set nums[i] = 0 if we already visited.
            slow = i
            while True:
                slow = next(slow)
                if nums[i] * nums[slow] <= 0:
                    break
                nums[slow] = 0
        return False