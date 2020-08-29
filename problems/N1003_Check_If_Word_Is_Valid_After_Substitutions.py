class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for letter in s:
            if letter != 'c':
                stack.append(letter)
                continue
            if len(stack) < 2 or stack[-1] != 'b' or stack[-2] != 'a':
                return False
            stack.pop()
            stack.pop()

        if not stack:
            return True
        else:
            return False
