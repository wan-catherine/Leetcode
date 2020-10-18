class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        data = list(zip(ages, scores))
        length = len(data)
        data.sort()

        dp = [0] * length
        for i in range(length):
            score = data[i][1]
            dp[i] = score
            for j in range(i):
                if data[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)
        return max(dp)
