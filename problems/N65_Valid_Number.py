class Solution:
    def isNumber_(self, s: str) -> bool:
        if not s:
            return False
        def is_integer(st):
            for i, c in enumerate(st):
                if c not in '0123456789+-':
                    return False
                if c in '+-' and (i != 0 or len(st) == 1):
                    return False
            return True
        ie,id,si = -1, -1, -1
        n = False
        for i, c in enumerate(s):
            if c not in '0123456789+-.eE':
                return False
            if c == '.':
                if id == -1:
                    id = i
                else:
                    return False
            elif c in 'eE':
                if ie == -1:
                    ie = i
                else:
                    return False
            elif c in '+-':
                if i == 0 or i == ie + 1:
                    continue
                else:
                    return False
            else:
                n = True
        if not n:
            return False
        if ie != -1 :
            if (not s[ie+1:] or not is_integer(s[ie+1:])):
                return False
            for i, c in enumerate(s[:ie]):
                if c in '0123456789':
                    break
            else:
                return False
        if id != -1:
            v = len(s) if ie == -1 else ie
            for i,c in enumerate(s[:v]):
                if c in '0123456789':
                    return True
            return False
        return True

    """
    DFA
    """
    def isNumber(self, s: str) -> bool:
        # states
        start = 0
        int_sign = 1
        integer = 2
        point = 3
        frac = 4
        exp = 5
        exp_sign = 6
        exp_int = 7

        # inputs
        digit = 1
        sign = 2
        dot = 3
        e = 4

        def classify(c):
            if c in '0123456789': return digit
            if c == '.': return dot
            if c in '+-': return sign
            if c in 'eE': return e
            raise ValueError

        machine = {
            start: {sign: int_sign, digit: integer, dot: point},
            int_sign: {digit: integer, dot: point},
            integer: {digit: integer, dot: frac, e: exp},
            point: {digit: frac},
            frac: {digit: frac, e: exp},
            exp: {digit: exp_int, sign: exp_sign},
            exp_sign: {digit: exp_int},
            exp_int: {digit: exp_int},
        }

        state = start
        for c in s.strip():
            try:
                state = machine[state][classify(c)]
            except:
                return False
        return state in [integer, frac, exp_int]