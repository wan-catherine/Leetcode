import collections


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        counter = collections.Counter(senate)
        senates = [[s, 0] for s in senate]
        length = len(senate)
        i = 0
        r, d = 0, 0
        while counter['R'] > 0 and counter['D'] > 0:
            i %= length
            if senates[i][1] == 1:
                i += 1
                continue
            if senates[i][0] == 'R':
                if r > 0:
                    r -= 1
                    senates[i][1] = 1
                    continue
                counter['D'] -= 1
                d += 1
            else:
                if d > 0:
                    d -= 1
                    senates[i][1] = 1
                    continue
                counter['R'] -= 1
                r += 1
            i += 1
            if counter['D'] <= 0:
                return 'Radiant'
            if counter['R'] <= 0:
                return 'Dire'
        if counter['D'] <= 0:
            return 'Radiant'
        if counter['R'] <= 0:
            return 'Dire'
