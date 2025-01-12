class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        if length % 2 != 0:
            return False

        lower, upper = 0, 0
        for i in range(length):
            if locked[i] == '1':
                if s[i] == '(':
                    lower += 1
                    upper += 1
                else:
                    lower -= 1
                    upper -= 1
            else:
                upper += 1
                lower -= 1
            if lower < 0:
                lower += 2
            if upper < 0:
                return False
        return lower == 0
