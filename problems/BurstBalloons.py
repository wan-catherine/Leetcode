class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        l = len(nums)

        res = [[0]* l for i in nums]

        n = 1
        while n <= l:
            for i in range(l):
                if i + n > l:
                    continue
                maxN = 0
                for j in range(n):
                    temp = nums[i+j]
                    if i > 0:
                        temp *= nums[i-1]
                    if l - i - n > 0:
                        temp *= nums[i+n]
                    if j == 0 and i + 1 < l:
                        temp += res[i+1][i+n-1]
                    if j + 1 == n:
                        temp += res[i][i+n-2]
                    if j > 0 and j < n - 1:
                        temp += res[i][i+j-1] + res[i+j+1][i+n-1]
                    maxN = max(temp, maxN)

                res[i][i+n-1] = maxN
            n += 1
        return res[0][-1]


