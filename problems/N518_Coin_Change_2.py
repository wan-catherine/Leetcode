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

    # d[i][j] : by using the first i coins, the totally amount is j, then it means the number
    # of coins that make up that amount j
    # d[i][j] seperate two situations :
    #         1. not used the ith coin : d[i-1][j]
    #         2. used the ith coin : d[i][j - coins[i-1]]
    # d[i][j] = d[i-1][j] + d[i][j-coins[i-1]]
    # Here because we can reuse the number in coins, so for the second situation
    # it will be d[i], because the coins there is infinite
    # also need to check if j - coins[i-1] >= 0

    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for i in range(1, len(coins) +1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[j] += dp[j - coins[i-1]]
        return dp[-1]