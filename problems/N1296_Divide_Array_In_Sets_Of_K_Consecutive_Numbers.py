class Solution(object):
    def isPossibleDivide_timeout(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        length = len(nums)
        if length % k:
            return False

        nums.sort()
        batch = []
        while nums:
            i = 0
            if batch:
                while nums[i] != batch[-1] + 1:
                    i += 1
                    if i >= len(nums):
                        return False
                    if nums[i] > batch[-1] + 1:
                        return False

            batch.append(nums[i])
            del nums[i]
            if not len(batch) % k:
                batch = []
        return True
    """
    Key point :
        find the head of the subarray: number is the head of subarray as long as (number-1)'s count is zero.
        For example:
        nums = [1,2,3,3,4,4,5,6], k = 4
        1 is the head 
        after get the first subarray 1,2,3,4
        then (3-1)'s count is zero, so 3 is the next subarray's head
        
    Here I use dictionary to save the number's count, it's  possible that we have one number which is head and it's count > 1
    For example : 1,1,2,2,3,3, k = 3
    So here we need to put (1,1) into the heads.
        
    """
    def isPossibleDivide(self, nums, k):
        if not nums:
            return False

        num_count_mapping = {}
        for num in nums:
            if num not in num_count_mapping:
                num_count_mapping[num] = 1
            else:
                num_count_mapping[num] += 1

        # find the head number which doesn't has number-1 . 1->2->3 , 1 is the head number which doesn't have 1-1 == 0 in the array.
        heads = []
        for num in num_count_mapping:
            if num-1 not in num_count_mapping:
                for i in range(num_count_mapping[num]):
                    heads.append(num)

        while heads:
            head = heads.pop()
            if num_count_mapping[head] == 0:
                continue
            for i in range(k):
                if head + i not in num_count_mapping or num_count_mapping[head+i] == 0:
                    return False
                num_count_mapping[head+i] -= 1
                if head+i+1 in num_count_mapping and num_count_mapping[head+i] == 0:
                    for _ in range(num_count_mapping[head+i+1]):
                        heads.append(head+i+1)
        if sum(num_count_mapping.values()) > 0:
            return False
        return True
        