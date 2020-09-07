class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split()
        lens = [len(word) for word in words]
        max_len = max(lens)
        res = []
        index = 0
        while index < max_len:
            temp = []
            for i, word in enumerate(words):
                if index < lens[i]:
                    temp.append(word[index])
                else:
                    temp.append(' ')
            res.append(''.join(temp).rstrip())
            index += 1
        return res