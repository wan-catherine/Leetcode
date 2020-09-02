import collections


class Solution:
    def containsNearbyAlmostDuplicate_before(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        length = len(nums)
        if nums == None or length < 1 :
            return False
        #this lien is the key part to pass all test cases and avoid TLE!!!
        if len(set(nums)) == length and t == 0:
            return False

        res = False
        for i in range(length):
            if i + k >= length:
                res = self.check(nums[i:], t)
            else:
                res = self.check(nums[i:i+k+1], t)
            if res:
                return res

        return res


    def check(self, nums, t):
        if len(nums) < 2:
            return False
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= t:
                return True
        return False

    def containsNearbyAlmostDuplicate_before(self, nums, k, t):
        if not nums:
            return False
        length = len(nums)
        if length < 2:
            return False
        if len(set(nums)) == length and t == 0:
            return False
        start, end = 0, 1
        while start < length:
            if end - start <= k:
                p = start + 1
                while p <= end:
                    if abs(nums[p] - nums[start]) <= t:
                        return True
                    p += 1
            if end - start == k or end == length - 1:
                start += 1
            if end < length - 1:
                end += 1
            # print(start, end)
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        length = len(nums)
        buckets = collections.OrderedDict()
        model = t + 1
        for i in range(length):
            key = nums[i] // model
            if key in buckets:
                return True
            if key - 1 in buckets and abs(buckets[key-1]-nums[i]) < model:
                return True
            if key + 1 in buckets and abs(buckets[key+1]-nums[i]) < model:
                return True
            buckets[key] = nums[i]
            if i >= k:
                del buckets[nums[i-k] // model]
        return False

