class Solution(object):
    def numSubarrayProductLessThanK_self(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        res = 0
        length = len(nums)
        left,right = 0, 1
        last_product = 1
        if last_product > k:
            return 0
        for i in range(0, length):
            left, last_product = self.get_left_index_and_product(nums, k, left, i, last_product)
            res += i - left + 1 if i >= left else 0
        return res

    def get_left_index_and_product(self, nums, k, left, right, last_product):
        last_product *= nums[right]
        if last_product < k:
            return (left, last_product)
        while last_product >= k:
            if left < 0 or left >= len(nums):
                break
            last_product //= nums[left]
            left += 1
        return (left, last_product)

    """
    How to understand : res += i - left + 1
    Each time, when we include a new element , the it means we can get i - left + 1 new subarray . 
    For example : [1,2,3] , then we add [4], it can get [4],[3,4],[2,3,4],[1,2,3,4]. 
    """
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1 or not nums:
            return 0

        left = 0
        temp = 1
        res = 0
        for i in range(len(nums)):
            temp *= nums[i]
            while temp >= k:
                temp //= nums[left]
                left += 1
            res += i - left + 1
        return res
