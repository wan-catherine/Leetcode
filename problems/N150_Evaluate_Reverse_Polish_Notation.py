"""
Round towards zero in integer division:
    python 3 : int(x/y)
        >>> int(-1 / 2)
        0
        >>> int(-3 / 2)
        -1
        >>> int(1 / 2)
        0
        >>> int(3 / 2)
        1

    python 2 : int(float(x)/y)
        >>> int(float(-1) / 2)
        0
        >>> int(float(-3) / 2)
        -1
        >>> int(float(1) / 2)
        0
        >>> int(float(3) / 2)
        1
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0

        stack = []
        for s in tokens:
            if s in "+-*/":
                right = int(stack.pop())
                left = int(stack.pop())
                if s == "+":
                    stack.append(right+left)
                elif s == "-":
                    stack.append(left - right)
                elif s == "*":
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(s)
        return stack[-1]
