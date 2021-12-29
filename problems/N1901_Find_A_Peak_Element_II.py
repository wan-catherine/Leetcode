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

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        l, r = 0, m

        def helper(r):
            c = 0
            for i in range(1, n):
                if mat[r][i] > mat[r][c]:
                    c = i
            return c

        while l < r:
            mid = (r - l) // 2 + l
            mmax = max(mat[mid])
            umax = -1 if mid == 0 else max(mat[mid - 1])
            dmax = -1 if mid == m - 1 else max(mat[mid + 1])
            maximum = max(mmax, umax, dmax)
            if maximum == mmax:
                return [mid, helper(mid)]
            if maximum == umax:
                r = mid
            else:
                l = mid + 1
