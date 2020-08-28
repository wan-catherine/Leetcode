class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if not S or not targets:
            return S
        length = len(indexes)
        mapping = {}
        for i in range(length):
            mapping[indexes[i]] = (sources[i], targets[i])

        indexes.sort()
        res = []
        prev = 0
        for i in range(length):
            index = indexes[i]
            source, target = mapping[index]
            if S[index:index+len(source)] == source:
                res.append(S[prev:index])
                res.append(target)
                prev = index + len(source)
        if prev < len(S):
            res.append(S[prev:])
        return ''.join(res)


