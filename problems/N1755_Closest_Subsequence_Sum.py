import bisect
"""
if len(nums) < 20, then we can use brute force , the time complexity is O(2**len(nums)) 
for getting all sums of subsets.

if the possible sum is around a small range([0,1000], then we can use dp as the knapsack problem.
dp = [0]* (len of set of sum)
dp[sum] = dp[sum-nums[i]]

but here the sum's range is very large and the len(nums) <= 40. so we need to split it into two 
arrays , then get sums of subset of each array, then use two sum method to get the results.

we need to get two sorted array of sums.
here we can loop one sums of subset and use binary search to find the closest value in second array.

we can use linear method. 
loop one from the start(i=0) and loop another one from end(j=len(arr2)), then:
    1. value == goal : best , diff == 0
    2. value > goal, then j -= 1
    3. value < goal, then i+= 1
"""

class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        length = len(nums)
        left, right = nums[:length//2], nums[length//2:]

        def get_sums(arr):
            sums = [0]
            length = len(arr)
            for k in range(length):
                temp = [v + arr[k] for v in sums]
                i, j, l = 0, 0, len(temp)
                ans = []
                while i < l and j < l:
                    if sums[i] < temp[j]:
                        ans.append(sums[i])
                        i += 1
                    else:
                        ans.append(temp[j])
                        j += 1
                if i < l:
                    ans.extend(sums[i:])
                if j < l:
                    ans.extend(temp[j:])
                sums = ans
            return sums

        lsums, rsums= get_sums(left), get_sums(right)
        diff = abs(goal)
        # ll = len(rsums)
        # for v in lsums:
        #     t = goal - v
        #     index = bisect.bisect_left(rsums, t)
        #     if index == ll:
        #         diff = min(diff, abs(rsums[index-1]+v - goal))
        #         continue
        #     if index < ll:
        #         diff = min(diff, abs(rsums[index]+v-goal))
        #     if index < ll + 1:
        #         diff = min(diff, abs(rsums[index-1]+v-goal))
        i, j = 0, len(rsums)-1
        while i < len(lsums) and j >=0:
            cur = lsums[i] + rsums[j]
            diff = min(diff, abs(cur-goal))
            if cur > goal:
                j -= 1
            elif cur < goal:
                i += 1
            else:
                return 0
        return diff
