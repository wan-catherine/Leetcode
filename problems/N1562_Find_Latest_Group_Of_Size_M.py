import collections
from collections import deque

"""
During the contest , I actually wrote all the necessary steps . use the list to save all intervals and use binary search to find the 
right intervals , then split it again, at the same time, update the groups information. 
But timeout!!!

KEY POINT:
I found if the len(interval) < m , then there is no need to add it into the list . This actually save a lot of time.
"""
class Solution(object):
    def findLatestStep_myself(self, arr, m):
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

    """
    O(N)
    Key point : 
        We don't need to update all position from [i, j] to the latest length. We only care about the leftmost and rightmost .
        Because for all other in the middle, we won't use the value again. All we care about the border value. 
        So we can only update sizes[pos-left], sizes[pos+right]
    """
    def findLatestStep_n(self, arr, m):
        length = len(arr)
        count = [0] * (length + 1)
        sizes = [0] * (length + 2)
        res = -1
        for i, pos in enumerate(arr):
            left, right = sizes[pos-1], sizes[pos+1]
            sizes[pos], sizes[pos-left], sizes[pos+right] = [right + left + 1] * 3
            count[left] -= 1
            count[right] -= 1
            count[right+left+1] += 1
            if count[m] > 0:
                res = i + 1
        return res

    """
    Sliding windows 
    use a window to track the length of '1''s most day. 
    
    days[i] means set ith position to '1' at days[i] (from 1-index)
    
    """
    def findLatestStep(self, arr, m):
        length = len(arr)
        if m == length:
            return length

        days = [0] * (length + 1)
        for i, pos in enumerate(arr):
            days[pos] = i + 1

        queue = deque()
        res = -1
        for i in range(1, length+1):
            while queue and days[queue[-1]] < days[i]:
                queue.pop()
            while queue and i - queue[0] >= m:
                queue.popleft()
            queue.append(i)
            if i < m:
                continue

            max_day = days[queue[0]]
            left, right = 10**6, 10**6 # this is a great way to deal with boarder condition
            if i - m >= 1:
                left = days[i-m]
            if i + 1 <= length:
                right = days[i+1]
            if max_day < left and max_day < right:
                res = max(res, min(left, right) - 1)
        return res

