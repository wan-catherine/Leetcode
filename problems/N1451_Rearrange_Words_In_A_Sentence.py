import collections


class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        words = text.split()
        words[0] = words[0].lower()
        mapping = collections.defaultdict(list)
        for word in words:
            mapping[len(word)].append(word)
        keys = sorted(mapping.keys())
        res = []
        for key in keys:
            res.extend(mapping[key])
        res[0] = res[0].capitalize()
        return ' '.join(res)