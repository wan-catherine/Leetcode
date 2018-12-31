class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words == None or len(words) < 2:
            return 0

        number = [0] * len(words)
        for i in range(len(words)):
            for c in words[i]:
                number[i] |= (1 << (ord(c) - 97))

        res = 0
        for i in range(len(words)):
            for j in range(i+ 1, len(words)):
                if number[i] + number[j] == (number[i] | number[j]):
                    res = max(res, len(words[i]) * len(words[j]))

        return res
