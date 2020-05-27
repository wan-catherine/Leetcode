"""
This is an amazing question, so beautiful!!!

Use binary search
use the smallest number and largest number in the matrix to find a number which has k numbers less or equal to them.

Here are two key points here :
1. when we write function count_of_numbers_less_or_equal, notice the rows and columns are sorted in ascending order which
    means the numbers maybe equal between two adjacent numbers
2. when we get count which equals to k , at this time, mid maybe not in the matrix. There are two situations :
    a. mid in the matrix , so we can directly return it
    b. mid not in the matrix and it only can between a < mid < b , a and b are in the matrix and should be adjacent numbers.

    so we need to keep shrink the range of lo and hi : hi = mid

    here also notic : mid = lo + (hi - lo) // 2
    if we want to shrink the range, two ways to do :
        a. lo = mid + 1
        b. hi = mid

    the reason for this is (hi - lo) // 2 might eaquals to zero, which means the mid might equals to lo , so we need to make sure :
        lo = mid + 1
    for hi , then if lo + 1 = hi , hi = mid will shrink the range . if lo + 1 < hi, it obviously also shrink the range.
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        self.matrix = matrix
        self.length = len(matrix)
        lo = matrix[0][0]
        hi = matrix[self.length-1][self.length-1]

        while lo < hi:
            mid = lo + (hi - lo) // 2
            count = self.count_of_numbers_less_or_equal(mid)
            if count >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


    def count_of_numbers_less_or_equal(self, m):
        count = 0
        i,j = self.length-1, 0
        while j < self.length and i >= 0:
            if m >= self.matrix[i][j]:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count


