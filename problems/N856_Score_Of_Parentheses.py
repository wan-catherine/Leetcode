class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0

        length = len(S)
        stack = []
        for i in range(length):
            if not stack or S[i] == '(':
                stack.append(S[i])
                continue

            if stack[-1] == '(':
                stack.pop()
                if stack:
                    if isinstance(stack[-1], int):
                        val = stack.pop()
                        stack.append(val + 1)
                    else:
                        stack.append(1)
                else:
                    stack.append(1)
            else:
                val = stack.pop() * 2
                stack.pop()
                if stack and isinstance(stack[-1], int):
                    next = stack.pop()
                    stack.append(val + next )
                else:
                    stack.append(val)
        return stack[-1]

