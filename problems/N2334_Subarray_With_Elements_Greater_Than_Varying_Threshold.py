from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        length = len(nums)
        minimum = min(nums)
        if length * minimum > threshold:
            return length
        stack = []
        next, prev = [-1] * length, [-1] * length
        for i in range(length):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                next[index] = i - index
            stack.append(i)
        for i in range(length):
            if next[i] == -1:
                next[i] = length - 1 - i
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                index = stack.pop()
                prev[index] = index - i
            stack.append(i)
        for i in range(length):
            if prev[i] == -1:
                prev[i] = i
        for i in range(length):
            if nums[i] > threshold:
                return 1
            if (prev[i] + next[i] - 1) * nums[i] > threshold:
                return prev[i] + next[i] - 1
        return -1