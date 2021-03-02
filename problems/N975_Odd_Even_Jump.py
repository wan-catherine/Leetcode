import bisect
import collections

"""
Notice : 
For odd-numbered jumps, it asks the arr[j] is the smallest possbile value. 
For even-numbered jumps, it asks the arr[j] is the largest possbile value. 

So if the arr[j] == arr[i], then it means it can be both (odd/even) jumps
"""
class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        mapping = collections.defaultdict(list)
        mapping[arr[-1]].append(length-1)

        dp = [[False]*2 for _ in range(length)]
        dp[-1][0], dp[-1][1] = True, True
        stack = [arr[-1]]
        for i in range(length-2, -1 , -1):
            index = bisect.bisect_left(stack, arr[i])
            if index == len(stack):
                idx = mapping[stack[-1]][-1]
                dp[i][0] = dp[idx][1]
            elif index == 0:
                idx = mapping[stack[0]][-1]
                dp[i][1] = dp[idx][0]
                if stack[index] == arr[i]:
                    dp[i][0] = dp[idx][1]
            else:
                large = mapping[stack[index]][-1]
                if stack[index] == arr[i]:
                    small = large
                else:
                    small = mapping[stack[index-1]][-1]
                dp[i][1] = dp[large][0]
                dp[i][0] = dp[small][1]
            bisect.insort_left(stack, arr[i])
            mapping[arr[i]].append(i)
        res = 0
        for i in range(length):
            if dp[i][1] == True:
                res += 1
        return res