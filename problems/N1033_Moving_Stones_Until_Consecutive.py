"""
Minimum:
    1. when a,b,c is conseuquce : 1,2,3
    2. when ab c or a bc : 12 5, 1 45
    3. when a b    c or a   b c : 1 3 7, 1 4 6
    4. general situation a  b  c , then move a to b-1, c to b+1 , 1 5 8

Maximum:
    move one step each time : c - a - 2
    a   b    c  ---> c to a except b
"""
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        li = [a, b, c]
        li.sort()

        if li[0] + 1 == li[1] and li[1] + 1 == li[2]:
            m = 0
        elif li[0] + 1 == li[1] or li[1] + 1 == li[2]:
            m = 1
        elif li[0] + 2 == li[1] or li[1] + 2 == li[2]:
            m = 1
        else:
            m = 2

        return [m, li[2] - li[0] - 2]

