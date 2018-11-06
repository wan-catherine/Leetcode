class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == None or len(triangle) == 0 or len(triangle[0]) == 0:
            return 0

        res = triangle[0]
        for i in range(1, len(triangle)):
            temp = []
            for j in range(len(triangle[i])):
                if j == 0 :
                    temp.append(res[j]+ triangle[i][j])
                    continue
                if j == len(triangle[i]) - 1:
                    temp.append(res[j-1] + triangle[i][j])
                    continue
                temp.append(triangle[i][j] + min(res[j-1], res[j]))
            res = temp

        return min(res)

    #from last row to the first row
    def minimumTotal_better(self, triangle):
        lastRow = triangle[-1]

        for row in reversed(triangle[:-1]):
            tempRow = row[:]
            for i in range(0, len(row)):
                tempRow[i] += min(lastRow[i], lastRow[i + 1])
            lastRow = tempRow
        return lastRow[0]
