"""
for the timeout method, I use the same idea as 327.

For the second o(n) , we use sum_count_mapping: key: sum(nums[:i+1]), value: count of this sum
sum[i] = sum(nums[0:i+1]
sum[j] = sum(nums[0:j+1]
sum[j] - sum[i] = sum(nums[i+1:j+1])

if sum[j] = sum[i] + k,
then we know there is a subarray which sum(nums[i+1,j+1]) == k

"""
import bisect


class Solution(object):
    def subarraySum_timeout(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = [0] + nums
        nums_len = len(nums)
        for i in range(nums_len):
            sum[i+1] = sum[i] + nums[i]
        return self.merge_sort(sum, 0, nums_len, k)

    def merge_sort(self, sum, start, end, k):
        if start >= end:
            return 0
        mid = (end - start) // 2 + start
        count = self.merge_sort(sum, start, mid, k) + self.merge_sort(sum, mid+1, end, k)
        for i in range(start, mid + 1):
            for j in range(mid + 1, end+1):
                if sum[j] - sum[i] > k:
                    break
                if sum[j] - sum[i] == k:
                    count += 1
        self.merge(sum, start, mid + 1, end)
        return count

    def merge(self, sum, start, mid, end):
        cache = sum[:]
        l, r, index = start, mid, start
        while l < mid and r <= end:
            if cache[l] < cache[r]:
                sum[index] = cache[l]
                l += 1
            else:
                sum[index] = cache[r]
                r += 1
            index += 1
        while l < mid:
            sum[index] = cache[l]
            l += 1
            index += 1
        while r <= end:
            sum[index] = cache[r]
            r += 1
            index += 1

    # fastest one
    def subarraySum_hashtable(self, nums, k):
        sum = [0] + nums
        nums_len = len(nums)
        sum_count_mapping = {0:1}
        count = 0
        for i in range(nums_len):
            sum[i+1] = sum[i] + nums[i]
            if sum[i+1] - k in sum_count_mapping:
                count += sum_count_mapping[sum[i+1]-k]
            if sum[i+1] in sum_count_mapping:
                sum_count_mapping[sum[i+1]] += 1
            else:
                sum_count_mapping[sum[i+1]] = 1
        return count

    # use bisect.bisect to find the rightest position
    # use bisect.bisect_left to find the left-est postion
    # if there is no 'temp' in the prefex_sum array, the they are same, minor each other will return zero
    # so if there is no duplicated number but just one in the prefix_sum, they minor each other will return one
    # if there are duplicated numbers , then we will get the count of the number
    def subarraySum(self, nums, k):
        sum = 0
        prefix_sum = [0]
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            temp = sum - k
            count += bisect.bisect(prefix_sum, temp) - bisect.bisect_left(prefix_sum, temp)
            bisect.insort_left(prefix_sum, sum)
        return count
