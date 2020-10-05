import bisect

class Solution(object):
    def numSubseq_my(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        exclude = 1
        flag = False
        for i, num in enumerate(nums):
            if num >= target:
                flag = True
                break
            if 2 * num <= target:
                continue
            index = bisect.bisect_right(nums, target - num)
            if index == 0 and nums[index] != target - num:
                flag = True
                break
            if nums[index] == target - num:
                exclude += 2 ** (i - index - 1)
            else:
                exclude += 2 ** (i - index)
        if flag:
            res = 2 ** (i)
        else:
            res = 2 ** (i + 1)
        return (res - exclude) % (10 ** 9 + 7)

    # check all nums[i]
    # First from right side, find the largest nums[j] which nums[i] + nums[j] <= target
    # then for nums[i], all numbers betwee nums[i+1] ~ nums[j], we can choose pick or not pick then get a new subsequence with nums[i]
    # so, res += 2 ** (j-i)
    # loop all i.
    def numSubseq(self, nums, target):
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = (10**9+7)
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 2 ** (r - l) % mod
                l += 1
        return res % (10**9+7)
