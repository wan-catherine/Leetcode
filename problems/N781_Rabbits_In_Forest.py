import collections


class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0

        count = collections.Counter(answers)
        res = 0
        for key, value in count.items():
            res += (value // (key + 1)) * (key+1)
            res += (key + 1) if value % (key+1) else 0
        return res
