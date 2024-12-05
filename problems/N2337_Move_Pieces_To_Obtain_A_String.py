"""
    Check if start and target are same if without _'s;
    Check if all positions of L's in start are no smaller than those in target;
    Check if all positions of R's in start are no larger than those in target;
    If all above 3 are yes, return true; otherwise return false.
"""
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s, t, length = [], [], len(start)
        sindex, tindex = [], []
        for i in range(length):
            if start[i] != '_':
                s.append(start[i])
                sindex.append([start[i], i])
            if target[i] != '_':
                t.append((target[i]))
                tindex.append([target[i], i])
        if s != t:
            return False
        for i in range(len(sindex)):
            if sindex[i][0] == 'L' and sindex[i][1] < tindex[i][1]:
                return False
            if sindex[i][0] == 'R' and sindex[i][1] > tindex[i][1]:
                return False
        return True
