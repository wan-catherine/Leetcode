"""
For given val, how to count how many numbers which less or equal to val ?
It's multiplication table.

1   2   3   ...   n*1
2   4   6   ...   n*2
...
i 2*i  3*i  ...  n*i  <= x  (left and right side both //i )

m 2*m  3*m  ...  n*m

==> 1 2 3 ... n <= x//i
here s might be very large , so min(n, x//i)
"""
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_less_equal_than(val):
            nonlocal m,n, k
            count = 0
            for i in range(1, m+1):
                v = val // i
                if not v:
                    break
                count += min(n, v)
                if count >= k:
                    break
            return count

        left, right = 1, m*n + 1
        while left < right:
            mid = (right - left) // 2 + left
            if count_less_equal_than(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left