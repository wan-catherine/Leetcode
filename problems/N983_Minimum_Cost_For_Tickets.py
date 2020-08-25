"""
dp[i] = min{
            dp[i-1] + costs[0],
            dp[max(0, i-7)] + costs[1],
            dp[max(0, i-30)] + costs[2]
            }

Here are two key points:
    first: if i - 7 < 0 or i - 30 < 0 , we can buy one related ticket .
    second: if the day not in days, then we don't need to buy ticket , the cost should be same as dp[i-1]
"""
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        d_index = 0
        length = len(days)
        dp = [0] * (days[-1] + 1)
        for i in range(1, days[-1] + 1):
            if d_index >= length or i != days[d_index]:
                dp[i] = dp[i-1]
                continue
            d_index += 1
            dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
        print(dp)
        return dp[-1]



