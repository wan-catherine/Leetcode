import collections
import sys

"""
After get all valid subarray , we need to find a way to compare whether they are overlap or not. 
We maintain a min_len[i] which means : the minimum length of the subarray(ends with ith or before ith) which sum is target .
Then check all valid subarray, to find it's minimum satified previous subarray. 
"""
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        prefix = arr[:]
        length = len(arr)
        mapping = {0:-1, arr[0]:0}
        for i in range(1, length):
            prefix[i] += prefix[i-1]
            mapping[prefix[i]] = i
        res = collections.defaultdict(list)
        min_len = [0] * length
        minimum = sys.maxsize
        for i in range(length):
            min_len[i] = minimum
            val = prefix[i] - target
            if val in mapping:
                res[i - mapping[val]].append([mapping[val], i])
                minimum = min(minimum, i - mapping[val])
                min_len[i] = minimum

        if not res:
            return -1
        ans = sys.maxsize
        for key, li in res.items():
            for s, e in li:
                if s == -1:
                    continue
                if min_len[s] != sys.maxsize:
                    ans = min(ans, min_len[s] + key)

        return ans if ans != sys.maxsize else -1

