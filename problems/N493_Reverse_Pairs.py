import bisect


class Solution(object):
    def reversePairs_timeout(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_len = len(nums)
        if nums_len < 2:
            return 0
        sorted_nums = [nums[-1]]
        count = 0
        for i in range(nums_len-2, -1, -1):
            index = bisect.bisect(sorted_nums, nums[i])
            for j in range(index-1, -1, -1):
                if nums[i] > 2 * sorted_nums[j]:
                    count += j + 1
                    break
            bisect.insort(sorted_nums, nums[i])
        return count

    def reversePairs_still_timeout(self, nums):
        if not nums:
            return 0
        nums_len = len(nums)
        double_nums = [2 * nums[-1]]
        count = 0
        for i in range(nums_len - 2, -1, -1):
            index = bisect.bisect_left(double_nums, nums[i])
            count += index
            bisect.insort_left(double_nums, nums[i]*2)
        return count

    def reversePairs(self, nums):
        count = self.merge_sort(nums, 0, len(nums)-1)
        return count

    def merge_sort_timeout(self, sum, start, end):
        if end <= start:
            return 0
        mid = (end - start) // 2 + start
        count = self.merge_sort(sum, start, mid) + self.merge_sort(sum, mid + 1, end)

        index = mid+1
        for i in range(mid+1, end + 1):
            temp = bisect.bisect(sum, 2*sum[i], start, mid+1)
            if temp == mid+1:
                break
            count += index - temp
        self.merge(sum, start, mid + 1, end)
        return count

    def merge(self, sum, start, mid, end):
        cache = sum[:]
        l , r , index = start, mid, start
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

    def reversePairs(self, nums):
        if not nums:
            return 0

        return self.mergesort(nums)[1]

    def mergesort(self, nums):
        if len(nums) <= 1:
            return nums, 0
        m = len(nums) // 2
        left, countl = self.mergesort(nums[:m])
        right, countr = self.mergesort(nums[m:])
        count = countl + countr
        for r in right:
            # here need to use bisect.bisect
            # because for i < j , nums[i] > 2 * nums[j]
            # we use 2 * r here, so must get the left-est position to filter out the situation == 2*r.
            # see test_reversePairs
            temp = len(left) - bisect.bisect(left, 2 * r)
            if temp == 0:
                break
            count += temp

        return sorted(left + right), count