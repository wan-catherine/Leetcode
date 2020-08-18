class Solution(object):
    def calculate_mine(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        length = len(s)

        for i in range(length):
            if s[i] == ' ':
                continue
            if s[i] in '0123456789':
                if stack and isinstance(stack[-1], int):
                    val = stack.pop()
                    stack.append(val*10 + int(s[i]))
                else:
                    stack.append(int(s[i]))
            else:
                stack.append(s[i])
        length = len(stack)
        if length == 1:
            return stack[0]
        new_stack = []
        for i in range(length):
            if new_stack and new_stack[-1] in ['*', '/']:
                sign = new_stack.pop()
                left = new_stack.pop()
                val = left * stack[i] if sign == '*' else left // stack[i]
                new_stack.append(val)
            else:
                new_stack.append(stack[i])

        length = len(new_stack)
        if length == 1:
            return new_stack[0]
        res = new_stack[0]
        for i in range(1, length, 2):
            if new_stack[i] == '+':
                res += new_stack[i+1]
            else:
                res -= new_stack[i+1]
        return res

    def calculate(self, s):
        num = 0
        s += '+'
        length = len(s)
        stack, op = [], '+'
        for i in range(length):
            if s[i] == ' ':
                continue
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    val = stack.pop()
                    stack.append(num * val)
                else:
                    val = stack.pop()
                    stack.append(int(val / num))  # when val < 0 , val//num != int(val/num)
                op = s[i]
                num = 0
        return sum(stack)
