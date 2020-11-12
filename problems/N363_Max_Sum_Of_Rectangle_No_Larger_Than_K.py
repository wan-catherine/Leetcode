import bisect
import sys
"""
Classical problem:
1. For problems about matrix, we can think how to flat it . 
    a. brutal force time complexity is O(m*n*m*n), we need to fix left-most and right-most point to get a sub-matrix.
    b. we can fix up and down rows, then flat it into an array, then in this array, we use binary search to get the largest 
       number which close to k. Use the prefix-sum to get the intervals' sum.
2. Flat it with rows or cols ? 
   When we flat the matrix, the time complexity is O(m*m*nlgn), so in order to save more time, we can let n = max(rows, cols).
   So we will need to transpose the matrix.
3. In the get_sum function , we need to add zero in the sums array. So that we can get the presum[:i] itself!!!
"""

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        if rows > cols:
            matrix2 = [[0]*rows for _ in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    matrix2[j][i] = matrix[i][j]
            rows, cols = cols, rows
            matrix = matrix2

        def get_sum(arr):
            nonlocal k, cols
            sums, presum = [0], 0
            res = -sys.maxsize
            for i in range(cols):
                presum += arr[i]
                if presum == k:
                    return k
                val = presum - k
                index = bisect.bisect_left(sums, val)
                if index <= i:
                    res = max(res, presum - sums[index])
                bisect.insort_left(sums, presum)
            return res

        res = -sys.maxsize
        for up in range(rows):
            arr = [0] * cols
            for down in range(up, rows):
                for c in range(cols):
                    arr[c] += matrix[down][c]
                val = get_sum(arr)
                res = max(res, val)
        return res