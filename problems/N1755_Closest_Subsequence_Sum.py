import bisect


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
