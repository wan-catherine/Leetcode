"""
dp[i][l] : the number of ways that statisfied : string ends with index-i (zero-base) and length is l : num[i-l+1:i+1]
dp[i][l] = dp[i-1][1] + dp[i-2][2] + ... + dp[i-l-1][l-1]
    if nums[i-l-l+1:i-l+1] <= nums[i-l+1:i+1]:
        dp[i][l] += dp[i-l][l]
then we can see here actually a presum of dp.
dp[i][l] = presum_dp[i-1][l]

"""
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        length = len(num)
        presum_dp = [[0] * (length + 1) for _ in range(length)]
        # lcs = [[0] * (length + 1) for _ in range(length+1)]
        # for i in range(length-1, -1, -1):
        #     for j in range(length-1, -1, -1):
        #         if num[i] == num[j]:
        #             lcs[i][j] = lcs[i+1][j+1] + 1
        #         else:
        #             lcs[i][j] = 0
        for i in range(length):
            for l in range(1, i + 2):
                if l == i + 1 and num[0] != '0':
                    dp = 1
                else:
                    j = i - l
                    if num[j+1] == '0':
                        presum_dp[i][l] = presum_dp[i][l-1]
                        continue
                    if j - l + 1 >= 0:
                        maxl = l
                        # python : this way can pass all tests
                        if num[i-l+1:i+1] < num[j-l+1:j+1]:
                            maxl -= 1
                        # this way TLE!!!
                        # il = lcs[i-l+1][j-l+1]
                        # if il < maxl and num[i-l+1+il] < num[j-l+1+il]:
                        #     maxl -= 1
                    else:
                        maxl = j + 1
                    while num[j - maxl + 1] == '0':
                        maxl -= 1
                    dp = presum_dp[i-l][maxl]
                presum_dp[i][l] = presum_dp[i][l-1] + dp
        return presum_dp[length-1][length] % (10**9 + 7)
