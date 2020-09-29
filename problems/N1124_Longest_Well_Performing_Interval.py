"""
smiliar as 962. Maximum Width Ramp
Use a monotonic stack

1. use 1 as tiring and -1 as non-tiring
2. use the prefix to get the diff of tiring and non-tiring.
3. we need to insert 0 in prefix sum array, because here it asks strictly greater.
4. maintain a monotonic decreasing stack
5. loop the prefix sum array from the end, compare with the stack[-1]:
    a. if prefix[i] > stack[-1], it satisfied, get the distance and stack.pop(). Here i will be close to start, so the distance here is the
       largest one for stack[-1], after this , it can pop out.
    b. if not , then i--

"""
class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        res = 0
        arr = []
        for h in hours:
            if h > 8:
                arr.append(1)
            else:
                arr.append(-1)
        prefix = arr[:]
        length = len(arr)
        for i in range(1, length):
            prefix[i] += prefix[i-1]

        prefix.insert(0, 0)
        stack = []
        for i in range(length+1):
            if not stack or prefix[stack[-1]] > prefix[i]:
                stack.append(i)

        for i in range(length, -1, -1):
            while stack and prefix[stack[-1]] < prefix[i]:
                res = max(res, i - stack[-1])
                stack.pop()
        return res