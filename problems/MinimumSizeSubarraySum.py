class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        count = 0
        for i in nums:
            sum += i
            count+=1
            if sum >= s:
                break
        if sum < s:
            return 0
        if count == 1:
            return count
        start = 0
        end = count-1
        res = count
        i = 1

        while i < len(nums) :
            if res > end - start + 1:
                res = end -start + 1
            if end + 1 < len(nums) and nums[end+1] >= s:
                return 1
            if sum - nums[start] >= s:
                sum -= nums[start]
                start += 1
                i+=1
                continue
            if end + 1 < len(nums) and sum + nums[end+1] - nums[start]>= s:
                sum = sum + nums[end + 1] - nums[start]
                start+=1
                end+=1
                i+=1
                continue
            if end + 1 < len(nums):
                sum += nums[end+1]
                end+=1
            i+=1
        return res




