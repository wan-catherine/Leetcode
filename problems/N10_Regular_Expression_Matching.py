"""
d[i][j] means use the first i letters and first j letters to check if it matches or not.
here we need to consider the base situation : i = 0 or j = 0
    if : i == 0 and j == 0, it means empty string matches empty pattern --> d[0][0] = True
    elif : i > 0 and j == 0, it means empty pattern with non-empty string, it obviously all False --> d[i][0] = False
    else : i == 0 and j > 0 , it means empty string with non-empty pattern. There are two situations (p[j-1] never be ''):
        1. p[j-1] == '*' : d[i][j]=d[0][j]=d[0][j-2]
        2. p[j-1] != '*' : d[i][j]=d[0][j]=False

status transform formula:
d[i][j] (i > 0, j > 0):
    if p[j-1] in [s[i-1], '.'], this means the p[j-1] matches s[i-1], then it will same as d[i-1][j-1]:
        d[i][j] = d[i-1][j-1]
    elif p[j-1] == '*', then we need to check the letter before '*':
        if p[j-2] in [s[i-1],'.'], it means p[j-2] matches s[i-1], here we need to notice , there are two different situations :
            match one time : d[i][j] = d[i-1][j]  or
            match zero time : d[i][j] = d[i][j-2]  --> check test_isMatch_6
            so : d[i][j] = d[i-1][j] or d[i][j-2]
         else: at this time, it means p[j-2] doesn't match s[i-1], we need to move two position j-2
            if j >= 2: d[i][j] = d[i][j-2]
            else: d[i][j] = False  empty pattern can't match non-empty string
    else:
        d[i][j] = False  p[j-1] != s[i-1]

I tried four time and finally accepted .
The failed reason is the base situation. In the status transform formula, we use j-2, i-1, so when need to check when i=0,j=0 or 1.
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True

        dp_table = [[None for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp_table[0][0] = True
        for i in range(1, len(s) + 1):
            dp_table[i][0] = False

        for j in range(1, len(p) + 1):
            if p[j-1] == '*':
                dp_table[0][j] = dp_table[0][j-2]
            else:
                dp_table[0][j] = False

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] in [s[i-1], '.']:
                    dp_table[i][j] = dp_table[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] in [s[i-1], '.']:
                        dp_table[i][j] = dp_table[i-1][j] or dp_table[i][j-2]
                    elif j >= 2:
                        dp_table[i][j] = dp_table[i][j-2]
                    else:
                        dp_table[i][j] = False
                else:
                    dp_table[i][j] = False

        return dp_table[-1][-1]