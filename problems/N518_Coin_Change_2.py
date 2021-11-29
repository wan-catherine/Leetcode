from typing import List


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

    """
    Knapsack: 
    
    d[i][j] : by using the first i coins, the totally amount is j, then it means the number
    of coins that make up that amount j
    dp[i][j] separate two situations :
            1. not used the ith coin : dp[i-1][j]
            2. used the ith coin k times (k * coins[i-1] <= j) :  c = coins[i-1]                
                dp[i-1][j - c] + dp[i-1][j - 2*c] + dp[i-1][j - 3*c] + ... + dp[i-1][j - k*c] 
                
    so from #1 and # 2 , we can know : 
        dp[i][j] = dp[i-1][j] + dp[i-1][j - c] + dp[i-1][j - 2*c] + dp[i-1][j - 3*c] + ... + dp[i-1][j - k*c] 
    here we can do optimize:
        dp[i][j-c] =            dp[i-1][j - c] + dp[i-1][j - 2*c] + dp[i-1][j - 3*c] + ... + dp[i-1][j - k*c]
        
    ==> dp[i][j] = dp[i-1][j] + dp[i][j-c] 
    ==> dp[j] = dp[j] + dp[j-c]
    ==> dp[j] += dp[j-c]
    """
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for i in range(1, len(coins) +1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[j] += dp[j - coins[i-1]]
        return dp[-1]

    def change_three_loop(self, amount: int, coins: List[int]) -> int:
        coins = [0] + coins
        length = len(coins)
        dp = [[0] * (amount+1) for _ in range(length)]
        dp[0][0] = 1
        for i in range(1, length):
            for j in range(amount+1):
                k = 0
                while k * coins[i] <= j:
                    dp[i][j] += dp[i-1][j - k*coins[i]]
                    k += 1
        return dp[-1][-1]

    def change_20210328(self, amount: int, coins: List[int]) -> int:
        coins = [0] + coins
        length = len(coins)
        dp = [[0] * (amount + 1) for _ in range(length)]
        dp[0][0] = 1

        for i in range(1, length):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]]
        return dp[-1][-1]