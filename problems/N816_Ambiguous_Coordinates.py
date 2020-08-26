class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)
        s = S[1:-1]
        res = []
        for i in range(1, length - 2):
            left = self.create(s[:i])
            right = self.create(s[i:])
            if not left or not right:
                continue
            for l in left:
                for r in right:
                    res.append("({0}, {1})".format(l, r))
        return res

    def create(self, word):
        length = len(word)
        if length == 1:
            return [word]
        if word[0] == '0' and word[-1] == '0':
            return None
        if word[0] == '0':
            return ['0' + '.' + word[1:]]
        if word[-1] == '0':
            return [word]
        res = [word]
        for i in range(1, length):
            res.append(word[:i] + '.' + word[i:])
        return res
