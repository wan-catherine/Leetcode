class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        index_mapping = [[-1,-1] for _ in range(26)]
        for i in range(length):
            index = ord(S[i]) - ord('a')
            if index_mapping[index][0] == -1:
                index_mapping[index][0] = i
                index_mapping[index][1] = i
            else:
                index_mapping[index][1] = i

        start, end = 0, 0
        res = []
        rightest = 0
        while end < length:
            left, right = index_mapping[ord(S[end]) - ord('a')]
            if right > rightest:
                rightest = right
            if end == rightest:
                res.append(end - start + 1)
                start = end + 1
            end += 1
        return res