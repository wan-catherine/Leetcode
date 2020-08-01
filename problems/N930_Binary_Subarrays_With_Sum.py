import collections
"""
AMAZING!!!
"""

class Solution(object):
    def numSubarraysWithSum_slide_windows_other(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        """
        atMost(S) = sum 0 to sum S, atMost(S-1) = sum 0 to sum S-1
        j-i+1 is the count of valid subarrays found
        """
        def atMost(S):
            if S < 0: return 0
            res = i = 0
            for j in range(len(A)):
                S -= A[j]
                while S < 0:
                    S += A[i]
                    i += 1
                res += j - i + 1
            print(res)
            return res

        return atMost(S) - atMost(S - 1)

    """
    prefix sum
    Key point is test : test_numSubarraysWithSum_1
    We can't calculate the prefix sum, then use pre_sum[i - S],then the test will failed. 
    
    Notice : pre can be same for different i in A.
    """
    def numSubarraysWithSum_prefix_sum(self, A, S):
        count = collections.Counter({0:1})
        pre, res = 0, 0
        for i in A:
            pre += i
            res += count[pre - S]
            count[pre] += 1
        return res

    def numSubarraysWithSum(self, A, S):
        return self.help(A, S) - self.help(A, S-1)

    def help(self, A, S):
        left, right, temp, res = 0, 0, 0, 0
        length = len(A)
        while right < length:
            temp += A[right]
            while temp > S and left <= right:
                temp -= A[left]
                left += 1
            res += right - left + 1
            right += 1
        return res


