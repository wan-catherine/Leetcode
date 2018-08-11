class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        length = len(pairs)
        if length < 2:
            return length

        res = [1] + [0] * (length - 1)

        pairs = sorted(pairs)

        for i in range(1, length):
            res[i] = res[i - 1]
            k = None
            for j in range(i - 1, -1, -1):
                if pairs[j][1] < pairs[i][0]:
                    k = j
                    break

            if k == None:
                r = 1
            else:
                r = 1 + res[k]
            res[i] = max(res[i], r)

        return res[length -1]

