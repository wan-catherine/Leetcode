from math import inf

class Solution(object):
    def coin_change_best(self, coins, amount):
        if not coins:
            return -1
        if not amount:
            return 0
        if amount in coins:
            return 1

        C = tuple(sorted(coins, reverse=True))

        length = len(C) - 1
        self.ans = float('inf')

        def find(coin, step, target):
            now_coin = C[coin]
            q, r = divmod(target, now_coin)

            if r == 0:
                self.ans = min(self.ans, step + q)
            elif coin < length and step + q + 1 < self.ans:
                for j in range(q, -1, -1):
                    find(coin + 1, step + j, target - j * now_coin)

        find(0, 0, amount)
        return self.ans if self.ans != float('inf') else -1

    # d[i][j] : by using the first i coins, the totally amount is j, then it means the fewest
    # number of coins that make up that amount j
    # d[i][j] seperate two situations :
    #         1. not used the ith coin : d[i-1][j]
    #         2. used the ith coin : d[i][j - coins[i-1]] + 1
    # d[i][j] = min( d[i-1][j] + d[i][j-coins[i-1]]+1)
    # Here because we can reuse the coin in coins, so for the second situation
    # it will be d[i], because the coins there is infinite
    # also need to check if j - coins[i-1] >= 0
    def coin_change(self, coins, amount):
        dp = [0] + [-1] * amount
        for i in range(1, len(coins) + 1):
            temp = dp[:]
            for j in range(1, amount + 1):
                res = float(inf)
                if temp[j] != -1:
                    res = min(res,temp[j])
                if j - coins[i-1] >= 0 and dp[j - coins[i-1]] != -1:
                    res = min(res, dp[j - coins[i-1]] + 1)
                dp[j] = -1 if res == float(inf) else res
        return dp[-1]

    def coin_change_before(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp_table =[0] * (amount + 1)
        for i in range(1,amount + 1):
            res = float(inf)
            for coin in coins:
                if i - coin < 0:
                    continue
                if i == coin:
                    res = 1
                    continue
                if dp_table[i - coin] != -1:
                    res = min(res, dp_table[i - coin] + 1)

            dp_table[i] = -1 if res == float(inf) else res
        print(dp_table)
        return dp_table[amount]

    def coin_change_by_memo(self, coins, amount):
        if amount == 0:
            return 0
        memo = {}
        self.dp(coins, amount, memo)
        return memo.get(amount, -1)


    def dp(self, coins, amount, memo):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in memo:
            print("here")
            return memo[amount]

        for coin in coins:
            next_times= self.dp(coins, amount - coin, memo)
            if next_times > -1:
                memo[amount] = min(memo.get(amount, float(inf)), next_times + 1)
        memo[amount] = memo.get(amount, -1)
        return memo[amount]



