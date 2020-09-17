class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        arr = [[1] * N for _ in range(N)]
        for i, j in mines:
            arr[i][j] = 0

        dp_up = [[0] * N for _ in range(N)]
        dp_down = [[0] * N for _ in range(N)]
        dp_left = [[0] * N for _ in range(N)]
        dp_right = [[0] * N for _ in range(N)]

        for i in range(N):
            if arr[0][i] :
                dp_up[0][i] = 1
            if i >=1 and arr[i][0]:
                dp_up[i][0] = dp_up[i-1][0] + 1
            if arr[i][0]:
                dp_left[i][0] = 1
            if i >= 1 and arr[0][i]:
                dp_left[0][i] = dp_left[0][i-1] + 1
            if arr[i][-1]:
                dp_right[i][-1] = 1
            if i >= 1 and arr[-1][-i-1]:
                dp_right[-1][-i-1] = dp_right[-1][-i] + 1
            if arr[-1][i]:
                dp_down[-1][i] = 1
            if i >= 1 and arr[-i-1][-1]:
                dp_down[-i-1][-1] = dp_down[-i][-1] + 1

        for row in range(1, N):
            for col in range(1, N):
                if arr[row][col]:
                    dp_up[row][col] = dp_up[row-1][col] + 1
                    dp_left[row][col] = dp_left[row][col-1] + 1

                if arr[N-row-1][N-col-1]:
                    dp_down[N-row-1][N-col-1] = dp_down[N-row][N-col-1] + 1
                    dp_right[N-row-1][N-col-1] = dp_right[N-row-1][N-col] + 1
        res = 0
        for row in range(N):
            for col in range(N):
                if not arr[row][col]:
                    continue
                temp = min(dp_up[row][col], dp_down[row][col], dp_left[row][col], dp_right[row][col])
                res = max(res, temp)
        return res
