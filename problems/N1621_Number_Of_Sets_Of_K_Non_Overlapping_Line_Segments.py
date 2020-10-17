"""
Given n points, to find k segments which can share endpoints
It can change into : give n + k - 1 points, to find k segments which don't allow to share endpoints.
In order to get k segments , we need to choose 2 * k points from the total (n + k - 1) points .
So it's combination math problem : C(n+k-1, 2k).

Notice , how to organize the for loop!!!
"""
class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 1
        for i in range(1, 2*k+1):
            res *= n + k - i
            res /= i
        return res % (10 ** 9 + 7)