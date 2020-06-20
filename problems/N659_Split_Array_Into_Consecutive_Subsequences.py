import collections

"""
Use two dictionary:
one is num : count 
another one is : expected next number : count

We create 3 sequence first , then write the 4th number into the next_num_mapping 

"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        num_count_mapping = collections.defaultdict(int)
        for num in nums:
            num_count_mapping[num] += 1

        next_num_mapping = collections.defaultdict(int)
        for num in nums:
            if num_count_mapping[num] == 0:
                continue
            if next_num_mapping[num] > 0:
                num_count_mapping[num] -= 1
                next_num_mapping[num] -= 1
                next_num_mapping[num+1] += 1
                continue
            for i in range(3):
                if num_count_mapping[num+i] == 0:
                    return False
                num_count_mapping[num+i] -= 1
            next_num_mapping[num+3] += 1

        return True
