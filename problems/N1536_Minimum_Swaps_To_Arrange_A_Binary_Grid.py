class Solution:
    def minSwaps(self, grid) -> int:
        n = len(grid)
        arr = [0] * n
        for row in range(n):
            for col in range(n - 1, -1, -1):
                if grid[row][col]:
                    break
                arr[row] += 1

        ans = 0
        for i in range(n):
            target = n - i - 1
            if arr[i] >= target:
                continue
            flag = False
            for j in range(i + 1, n):
                if arr[j] >= target:
                    flag = True
                    ans += j - i
                    arr[i + 1:j + 1] = arr[i:j]
                    break
            if not flag:
                return -1
        return ans


