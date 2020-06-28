class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        start = 1
        if nums[0]:
            first, neg, pos = 1, 0, 1
        else:
            first, neg, pos = 0,-1,0
            for n in nums[1:]:
                if n == 0:
                    start += 1
                else:
                    break

        for i in range(start,len(nums)):
            if nums[i] == 0:
                neg += -1
                if nums[i] != nums[i-1]:
                    res.append(pos)
                    pos = 0
            else:
                pos += 1
                if nums[i] != nums[i-1]:
                    res.append(neg)
                    neg = 0
        res.append(pos) if pos > 0 else res.append(-1)

        maximum = 0
        one = 0
        has_zero = False
        for i in range(len(res)):
            if res[i] < 0:
                has_zero = True
            if res[i] == -1:
                temp = 0
                if i >= 1:
                    temp += res[i-1]
                if i+1 < len(res):
                    temp += res[i+1]
                maximum = max(maximum, temp)
            if res[i] > 0:
                maximum = max(maximum, res[i])
        if not has_zero:
            return res[0] - 1
        else:
            return maximum




