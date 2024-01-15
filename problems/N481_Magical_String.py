"""
need to give a base : 122
"""
class Solution:
    def magicalString(self, n: int) -> int:
        li = [1, 2, 2]
        i = 2
        while len(li) < n:
            if li[i] == 1:
                li.append(3 - li[-1])
            else:
                v = li[-1]
                li.append(3 - v)
                li.append(3 - v)
            i += 1
        res = 0
        for i in li[:n]:
            if i == 1:
                res += 1
        return res




