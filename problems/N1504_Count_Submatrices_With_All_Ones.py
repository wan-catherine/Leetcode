class Solution(object):
    def numSubmat_first(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        res = 0
        dp = [[0] * (cols + 1) for _ in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if mat[i-1][j-1] == 0:
                    continue
                # extend to left
                dp[i][j] = dp[i][j-1] + 1
                res += dp[i][j]

                #extend to up
                # we only need to check different rows for same col and get the minimum value
                # because this value means how many 1 for its left(include itself).
                # If it's 2 , it means there are two 1s. If i row itself has 2 ,then there are two more from up direction.
                minimum = dp[i][j]
                for k in range(i-1, 0, -1):
                    minimum = min(minimum, dp[k][j])
                    res += minimum
        return res

    # compress 2d metric to 1d array.
    def numSubmat(self, mat):
        rows, cols = len(mat), len(mat[0])
        res = 0
        for up in range(rows):
            status = [1] * cols
            for down in range(up, rows):
                for i in range(cols):
                    status[i] &= mat[down][i]
                res += self.count_one_row(status)
        return res

    def count_one_row(self, arr):
        res = 0
        count = 0
        for i in arr:
            if i == 0:
                count = 0
            else:
                count += 1
            res += count
        return res
