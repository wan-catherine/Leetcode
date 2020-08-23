import collections

"""
During the contest , I actually wrote all the necessary steps . use the list to save all intervals and use binary search to find the 
right intervals , then split it again, at the same time, update the groups information. 
But timeout!!!

KEY POINT:
I found if the len(interval) < m , then there is no need to add it into the list . This actually save a lot of time.
"""
class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        length = len(arr)
        if m == length:
            return length

        memo = collections.defaultdict(int)
        memo[length] = 1
        tuples = [(1,length)]
        for i in range(length - 1, -1, -1):
            index = self.helper(tuples, arr[i])
            if index == -1:
                continue

            l, r = tuples[index]
            new_tuples = []
            if arr[i] - l >= m :
                new_tuples.append((l, arr[i]-1))
                memo[arr[i] - l] += 1
            if r - arr[i] >= m:
                new_tuples.append((arr[i]+1, r))
                memo[r - arr[i]] += 1

            tuples[index:index+1] = new_tuples
            memo[r - l + 1] -= 1
            if m in memo and memo[m] > 0:
                return i
        return -1

    def helper(self, tuples, target):
        length = len(tuples)
        left, right = 0, length
        while left < right:
            mid = (right - left) // 2 + left
            l, r = tuples[mid]
            if l <= target and target <= r:
                return mid
            if target < l:
                right = mid
            else:
                left = mid + 1
        return -1

    def findLatestStep_timeout(self, arr, m):
        res = -1
        length = len(arr)
        groups = [0]*(length + 2)

        for i in range(1, length+1):
            index = arr[i-1]
            left, right = index - 1, index + 1
            l_num, r_num = groups[left], groups[right]
            groups[index-l_num:index+r_num+1] = [l_num + r_num + 1]*(l_num + r_num + 1)
            if m in groups:
                res = i
        return res

