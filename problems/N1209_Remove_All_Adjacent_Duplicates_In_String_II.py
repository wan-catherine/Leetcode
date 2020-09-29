class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i, 0])
            if stack[-1][0] == i:
                stack[-1][1] += 1

            if stack and stack[-1][1] >= k:
                if stack[-1][1] == k:
                    stack.pop()
                else:
                    stack[-1][1] -= k
        res = []
        for i,n in stack:
            if n > 0:
                res.append(i*n)
        return ''.join(res)
