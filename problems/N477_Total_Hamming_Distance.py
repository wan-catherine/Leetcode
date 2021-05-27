class Solution(object):
    def totalHammingDistance_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = 0
        mapping = {}
        for i in range(length):
            for j in range(i+1, length):
                if (nums[i], nums[j]) in mapping:
                    res += mapping[(nums[i], nums[j])]
                    continue
                num = nums[i] ^ nums[j]
                count = 0
                while num:
                    if num & 1 == 1:
                        count += 1
                    num >>= 1
                mapping[(nums[i], nums[j])] = count
                mapping[(nums[j], nums[i])] = count
                res += count
        # print(id_time)
        return res

    """
    count 0 and 1 in each bit . 
    for example, for ith bit, nums totally have x 0s, y 1s (x+y == len(nums))
    then the distance for this bit is x*y.
    For all distance = sum(each bit distance)
    """
    def totalHammingDistance(self, nums):
        res = 0
        for i in range(32):
            zero, one = 0, 0
            for num in nums:
                if (num >> i) & 1:
                    one += 1
                else:
                    zero += 1
            res += zero * one
        return res