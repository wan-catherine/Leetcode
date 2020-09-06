class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, v in enumerate(s):
            if v not in ['(', ')']:
                continue
            if v == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        li = []
        stack = set(stack)
        for i, v in enumerate(s):
            if i in stack:
                continue
            li.append(v)
        return ''.join(li)
