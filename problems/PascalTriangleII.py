class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        before = [1]
        for i in range(1,rowIndex+2):
            temp = [1]
            n = i - 2
            for j in range(n):
                temp.append(before[j] + before[j+1])
            temp.append(1)
            before = temp

        return before