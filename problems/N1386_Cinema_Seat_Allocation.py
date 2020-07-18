import collections


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserve = collections.defaultdict(list)
        for row, col in reservedSeats:
            reserve[row].append(col)

        res = 0

        for row in reserve:
            temp = [1] * 3
            for col in reserve[row]:
                if col in [2, 3]:
                    temp[0] = 0
                elif col in [8, 9]:
                    temp[2] = 0
                elif col in [4,5]:
                    temp[0] = 0
                    temp[1] = 0
                elif col in [6,7]:
                    temp[2] = 0
                    temp[1] = 0
            r = sum(temp)
            if r == 3:
                res += 2
            elif r == 0:
                res += 0
            else:
                res += 1

        res += (n - len(reserve)) * 2
        return res

