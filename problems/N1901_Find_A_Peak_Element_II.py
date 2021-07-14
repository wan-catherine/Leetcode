from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat) + 2, len(mat[0]) + 2
        mat = [[-1] + li + [-1] for li in mat]
        mat = [[-1] * cols] + mat + [[-1] * cols]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def helper(r, s, e):
            if s >= e:
                return None
            left, right = s, e
            mid = (right - left) // 2 + left
            ans = 0
            for i, j in directions:
                row, col = r + i, mid + j
                if mat[r][mid] > mat[row][col]:
                    ans += 1
                else:
                    break
            if ans == 4:
                return [r - 1, mid - 1]
            if mat[r][mid] < mat[r][mid - 1]:
                val = helper(r, s, mid)
                if val:
                    return val
            if mat[r][mid] < mat[r][mid + 1]:
                val = helper(r, mid + 1, e)
                if val:
                    return val
            if mat[r][mid] > mat[r][mid - 1] and mat[r][mid] > mat[r][mid + 1]:
                ans = 0
                for i, j in directions:
                    row, col = r + i, left + j
                    if mat[r][left] > mat[row][col]:
                        ans += 1
                    else:
                        break
                if ans == 4:
                    return [r - 1, left - 1]
                return helper(r, s + 1, e)

        for r in range(1, rows - 1):
            val = helper(r, 1, cols - 1)
            if val:
                return val

