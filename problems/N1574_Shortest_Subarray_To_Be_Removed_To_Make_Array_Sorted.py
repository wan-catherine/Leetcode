class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = len(arr) - self.helper(arr)
        return res

    def helper(self, arr):
        if not arr:
            return 0
        cur = 0
        length = len(arr)
        if length == 1:
            return 1
        for left in range(length - 1):
            if arr[left] <= arr[left+1]:
                left += 1
            else:
                break
        if left == length - 1:
            return length
        for right in range(length-1, 0, -1):
            if arr[right] >= arr[right - 1]:
                right -= 1
            else:
                break
        cur = max(cur, left + 1, length - right)
        i,j = left, right
        while i >= 0:
            if arr[i] > arr[right]:
                i -= 1
            else:
                break
        cur = max(cur, i+1 + length - right)
        while j < length:
            if arr[j] < arr[left]:
                j += 1
            else:
                break
        cur = max(cur, left + 1 + length - j)

        i, j = left, right
        while i >= 0 and j < length:
            if arr[i] > arr[j]:
                i -= 1
            elif arr[i] < arr[j]:
                j += 1
            else:
                cur = max(cur, i + 1 + length - j)
                break
        return cur