class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations.sort()
        length = len(citations)
        for i in range(length):
            if citations[i] >= length - i :
                return length - i
        return 0
