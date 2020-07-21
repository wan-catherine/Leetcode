class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        self.r_len = len(mat)
        self.c_len = len(mat[0])
        self.get_dp(mat)
        # return self.get_max(threshold)
        return self.get_max_binary_search(threshold)

    """
    This is the key point . 
    How to use DP to get the [x1,y1,x2,y2] square sum
    """
    def get_dp(self, mat):
        self.dp = [[0] * (self.c_len + 1) for _ in range(self.r_len + 1)]
        for i in range(1, self.r_len + 1):
            for j in range(1, self.c_len + 1):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + mat[i-1][j-1]


    def get_range_sum(self, left_r, left_c, right_r, right_c):
        return self.dp[right_r][right_c] - self.dp[left_r - 1][right_c] - self.dp[right_r][left_c - 1] \
               + self.dp[left_r - 1][left_c - 1]

    def get_max(self, threshold):
        ans = 0
        for i in range(1, self.r_len):
            for j in range(1, self.c_len):
                k = ans  # Notice, we can do prune, cause we need to return the maximum side-length
                while i + k <= self.r_len and j + k <= self.c_len:
                    if self.get_range_sum(i, j, i+k, j+k) > threshold:
                        break
                    ans = max(ans, k + 1)
                    k += 1
        return ans

    def get_max_binary_search(self, threshold):
        ans = 0
        for i in range(1, self.r_len):
            for j in range(1, self.c_len):
                left, right = 0, min(self.r_len - i, self.c_len - j) + 1
                while left < right:
                    mid = left + (right - left) // 2
                    if self.get_range_sum(i, j, i+mid, j+mid) > threshold:
                        right = mid
                    else:
                        left = mid + 1
                ans = max(ans, left + 1 - 1)  # +1 : left is base from zero and we need to ans based on 1, -1: it's left which is the smallest > threshold.
        return ans