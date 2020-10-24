"""
Create Gray Code:
0 : 0
1 : 0, 1
For all num > 1, how to create gray code:
    1. arr ==> arr + arr[::-1]
    2. the first half, add '0' before => keep it same as before
    3. the second half add '1' before => add 2*(i-1)
    
"""
class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        if n == 1:
            if start == 0:
                return [0, 1]
            else:
                return [1, 0]
        res = [0, 1]
        for i in range(2, n+1):
            arr = res[::-1]
            for j, v in enumerate(arr):
                arr[j] += 2 ** (i - 1)
            res.extend(arr)
        for i, v in enumerate(res):
            if v == start:
                break
        return res[i:] + res[:i]

