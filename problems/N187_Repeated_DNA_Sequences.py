import collections


class Solution(object):
    def findRepeatedDnaSequences_dict(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = collections.defaultdict(int)
        length = len(s)
        for i in range(length - 9):
            counter[s[i:i+10]] += 1
        return [key for key, value in counter.items() if value > 1]

    def findRepeatedDnaSequences(self, s):
        counter = set()
        res = set()
        length = len(s)
        for i in range(length - 9):
            temp = s[i:i+10]
            if temp in counter:
                res.add(temp)
            else:
                counter.add(temp)
        return list(res)