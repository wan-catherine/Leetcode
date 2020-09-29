class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type S: str
        :rtype: int
        """
        if not s:
            return 0

        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
