class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        def parse(s):
            x, n = 0, 0
            length, i = len(s), 0
            while i < length:
                if s[i] == 'x':
                    x += 1
                    i += 1
                elif s[i] in '+-':
                    sign = 1 if s[i] == '+' else -1
                    i += 1
                    cur = 0
                    flag = False
                    while i < length and s[i].isdigit():
                        flag = True
                        cur *= 10
                        cur += int(s[i])
                        i += 1
                    if i < length and s[i] == 'x':
                        x += cur*sign if flag else sign
                        i += 1
                    else:
                        n += cur * sign
            return [x, n]
        if left[0] not in '+-':
            left = '+' + left
        if right[0] not in '+-':
            right = '+' + right
        lx, ln = parse(left)
        rx, rn = parse(right)
        if ln == rn:
            if lx == rx:
                return "Infinite solutions"
            else:
                return "x=0"
        resx, resn = 0, 0
        if lx >= rx:
            resx, resn = lx - rx, rn - ln
        else:
            resx, resn = rx - lx, ln - rn
        if resx == 0 and resn != 0:
            return "No solution"
        return "x={0}".format(str(resn // resx))
