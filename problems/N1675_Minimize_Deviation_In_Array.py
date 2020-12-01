import heapq
"""
Key point:
    1. even number only can be reduced by divide 2
        even // 2 --> finally it will be get an odd number , odd number * 2 --> get back the same even number
        12//2 -> 6//2 -> 3*2 -> 6
    2. odd number only can be increased by multiply 2.
        odd * 2 --> even (even // 2) --> odd 
        3*2 -> 6 (6//2) -> 3, then all other operation will be show same number
        
From the up conclusion, we can know , in order to avoid duplicated calculate the number , we can do :
    1. all odd number * 2 --> even number 
    2. then only reduce all number and compare . 
    3. use priority queue to get the maximum number 
    4. update res = min(res, maximum - minimum)
    5. the end condition is the maximum is an odd number . because it can't be reduce any more. 
"""

class Solution(object):
    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            if nums[i] % 2:
                nums[i] *= 2
        minimum = min(nums)
        neq_nums = [-i for i in set(nums)]
        heapq.heapify(neq_nums)
        res = max(nums) - minimum
        while not abs(neq_nums[0]) % 2:
            val = abs(heapq.heappop(neq_nums))
            res = min(res, val - minimum)
            val //= 2
            heapq.heappush(neq_nums, -val)
            minimum = min(minimum, val)
        return min(res, abs(neq_nums[0]) - minimum)



