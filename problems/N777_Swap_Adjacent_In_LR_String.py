"""
Notice :
    XL => LX , not LX => XL
    RX => XR , not XR => RX
"""
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        sc, se = [], []
        length = len(start)
        for i in range(length):
            if start[i] != 'X':
                sc.append((start[i], i))
            if end[i] != 'X':
                se.append((end[i], i))

        scl, sel = len(sc), len(se)
        if scl != sel:
            return False
        for i in range(scl):
            if sc[i][0] != se[i][0]:
                return False
            if sc[i][0] == 'L' and sc[i][1] < se[i][1]:
                return False
            if sc[i][0] == 'R' and sc[i][1] > se[i][1]:
                return False
        return True

