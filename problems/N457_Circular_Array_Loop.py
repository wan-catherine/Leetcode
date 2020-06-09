"""
I read a lot of answers .
But still confused about how to decide to return True and how to end the loop.

We need to set nums[i] = 0 after we visit it.

"""
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
