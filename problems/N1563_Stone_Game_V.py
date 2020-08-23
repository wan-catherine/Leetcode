class Solution(object):
    def stoneGameV_(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        self.stoneValue = stoneValue
        memo = {}
        length = len(stoneValue)
        self.prefix_sum = [0]*(length+1)
        for i in range(length):
            self.prefix_sum[i+1] += self.prefix_sum[i] + stoneValue[i]

        res = self.helper(0, len(stoneValue)-1, memo)
        return res

    def helper(self, start, end, memo):
        if end == start:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]

        res = 0
        for i in range(start, end):
            prefix = self.prefix_sum[i+1] - self.prefix_sum[start]
            suffix = self.prefix_sum[end+1] - self.prefix_sum[i+1]
            if prefix < suffix:
                res = max(res, self.helper(start, i, memo) + prefix)
            elif prefix > suffix:
                res = max(res, self.helper(i+1, end, memo) + suffix)
            else:
                left = self.helper(start, i, memo) + prefix
                right = self.helper(i+1, end, memo) + suffix
                res = max(res, left, right)
        memo[(start,end)] = res
        return res

    def stoneGameV_slow(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        self.stoneValue = stoneValue
        memo = {}
        res = self.helper_slow(0, len(stoneValue), memo)
        # print(memo)
        return res

    def helper_slow(self, start, end, memo):
        length = end - start
        if length < 2:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]

        prefix_sum = self.stoneValue[start:end]
        suffix_sum = self.stoneValue[start:end]
        for i in range(1,length):
            prefix_sum[i] += prefix_sum[i-1]

        for i in range(length-2, -1, -1):
            suffix_sum[i] += suffix_sum[i+1]
        res = 0
        for i in range(start + 1, end):
            if prefix_sum[i-start-1] < suffix_sum[i-start]:
                res = max(res, self.helper(start, i, memo) + prefix_sum[i-start-1])
            elif prefix_sum[i-start-1] > suffix_sum[i-start]:
                res = max(res, self.helper(i, end, memo) + suffix_sum[i-start])
            else:
                left = self.helper(start, i, memo) + prefix_sum[i-start-1]
                right = self.helper(i, end, memo) + suffix_sum[i-start]
                res = max(res, left, right)
        memo[(start,end)] = res
        return res

