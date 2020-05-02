class Solution:
    def change_before(self, amount, coins):
        db_table = [[1] + [0] * amount]
        for index in range(len(coins)):
            row = [1]
            for col in range(amount):
                used, unused = 0, 0
                if col + 1 - coins[index] >= 0:
                    used = row[col + 1 - coins[index]]
                unused = db_table[index][col + 1]
                row.append(used + unused)
            db_table.append(row)
        return db_table[-1][-1]

    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for i in range(1, len(coins) +1):
            before_dp = dp[:]
            for j in range(1, amount+1):
                dp[j] = before_dp[j]
                if j - coins[i-1] >= 0:
                    dp[j] += dp[j - coins[i-1]]
        return dp[-1]