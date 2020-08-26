class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                temp = ''
                while stack and stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num_str = ''
                while stack and stack[-1] in '0123456789':
                    num_str = stack.pop() + num_str
                num = int(num_str)
                stack.append(temp*num)
        return ''.join(stack)

