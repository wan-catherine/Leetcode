class Solution(object):
    def maxScore_sliding_window(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length = len(cardPoints)
        win_len = length - k
        total = sum(cardPoints)
        sub = sum(cardPoints[:win_len])
        res = sub
        for i in range(1, length - win_len + 1):
            sub = sub - cardPoints[i-1] + cardPoints[i + win_len - 1]
            res = min(res, sub)
        return total - res


    """
    https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/598111/Java-dp-solution(explanation-with-picture)
    dp[0] : all k are in the right side 
    dp[i] : there are i cards from left side, and k - i cards from right side
    
    dp[i] = dp[i-1] + cardPoints[i-1] + cardPoints[i - k - 1]
        add a card from left, and remove a card from right(not the end of right)
    """
    def maxScore(self, cardPoints, k):
        length = len(cardPoints)
        dp = [0] * (k+1)
        dp[0] = sum(cardPoints[length - k:])
        res = dp[0]
        for i in range(1, k+1):
            dp[i] = dp[i-1] + cardPoints[i-1] - cardPoints[i - k - 1]
            res = max(res, dp[i])
        return res

