class Solution:
    def calculate(self, s: str) -> int:
        li = ['+']
        for c in s:
            if c == ' ':
                continue
            li.append(c)
            if c == '(':
                li.append('+')

        length = len(li)
        res, sign = 0, 1
        nums, opts = [], []
        i = 0
        while i < length:
            if li[i] in '+-':
                sign = 1 if li[i] == '+' else -1
                i += 1
            elif li[i].isdigit():
                v = 0
                while i < length and li[i].isdigit():
                    v *= 10
                    v += int(li[i])
                    i += 1
                v *= sign
                res += v
            elif li[i] == '(':
                nums.append(res)
                opts.append(sign)
                res = 0
                i += 1
            elif li[i] == ')':
                res = nums.pop() + opts.pop() * res
                i += 1
        return res
