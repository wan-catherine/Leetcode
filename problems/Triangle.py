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
