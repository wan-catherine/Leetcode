import collections


class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        length, l = len(words[0]), len(target)
        index_char_mapping = ['#']
        for i in range(length):
            d = collections.defaultdict(int)
            for word in words:
                d[word[i]] += 1
            index_char_mapping.append(d)

        dp = [[0]*(length+1) for _ in range(l+1)]
        for i in range(length+1):
            dp[0][i] = 1
        for i in range(1, l+1):
            for j in range(1, length+1):
                dp[i][j] = dp[i][j-1]
                if target[i-1] in index_char_mapping[j]:
                    dp[i][j] += dp[i-1][j-1] * index_char_mapping[j][target[i-1]]
        return dp[-1][-1] % (10**9+7)