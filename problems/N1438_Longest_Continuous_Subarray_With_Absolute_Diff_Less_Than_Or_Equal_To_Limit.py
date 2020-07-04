import bisect
import collections
from collections import deque


class Solution(object):
    def longestSubarray_self(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        left, right = 0, 0
        res = 0
        hi,lo = 0, 0
        length = len(nums)
        while right < length:
            res = max(res, right - left + 1)
            right += 1
            if right >= length:
                break
            if nums[right] >= nums[hi]:
                hi = right
            if nums[right] <= nums[lo]:
                lo = right

            # here is the place which can be optimized
            while nums[hi] - nums[lo] > limit:
                if hi < lo:
                    left = hi + 1
                    hi = left
                    temp = nums[hi]
                    for i in range(left, right+1):
                        if nums[i] >= temp:
                            hi = i
                            temp = nums[i]
                else:
                    left = lo + 1
                    temp = nums[left]
                    for i in range(left, right + 1):
                        if nums[i] <= temp:
                            lo = i
                            temp = nums[i]
        return res

    # DON'T UNDERSTAND ???
    def longestSubarray_bts(self, nums, limit):
        i, L = 0, []
        for j in range(len(nums)):
            bisect.insort(L, nums[j])
            if L[-1] - L[0] > limit:
                L.pop(bisect.bisect(L, nums[i]) - 1)
                i += 1
            print(L)
        print(j, i)
        return j - i + 1

    """
    Mononic stack
    This problem is a sliding window problem, the key point here is how to easily find the high and low value in the windows.
    We can easily brute force search the whole window and update the high and low value . like the first method . O(N^2)
    
    Or we can maiantian the window into some automatically sort contianer (treemap in java, multiset in c++)
    O(NlgN)
    
    The best is try O(1) time find the high and low in the window : mononic stack 
    
    """
    def longestSubarray_while(self, nums, limit):
        length = len(nums)
        maximum, minimum = deque(), deque()
        left, res = 0, 0
        for i in range(length):
            while maximum and nums[maximum[-1]] < nums[i]:
                maximum.pop()
            while minimum and nums[minimum[-1]] > nums[i]:
                minimum.pop()
            maximum.append(i)
            minimum.append(i)
            while nums[maximum[0]] - nums[minimum[0]] > limit:
                if nums[left] == nums[maximum[0]]:
                    maximum.popleft()
                if nums[left] == nums[minimum[0]]:
                    minimum.popleft()
                left += 1
            res = max(res, i - left + 1)
        return res

    """
    Use If not while here to main a sliding window which only grow never shrink. 
    If when A[i] is added in the window which cause > limit, then the window needs to keep same lenght
    so i (left) should plus 1. 
    
    """
    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i
