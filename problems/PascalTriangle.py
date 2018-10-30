class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(2,numRows+1):
            temp = [1]
            n = i - 2
            for j in range(n):
                temp.append(res[i-2][j] + res[i-2][j+1])
            temp.append(1)
            res.append(temp)

        return res