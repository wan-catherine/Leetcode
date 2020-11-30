class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        li = input.split(r'\n')
        stack = []
        res = 0
        for s in li:
            t = 0
            while s.startswith(r'\t'):
                t += 1
                s = s[2:]
            while stack and stack[-1][1] >= t:
                stack.pop()
            stack.append((s, t))
            if '.' in s:
                path = '/'.join(s[0] for s in stack)
                res = max(res, len(path))
        return res

