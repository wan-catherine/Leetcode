from math import inf

class Solution(object):
    def coin_change(self, coins, amount):
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

    def coin_change_by_dp_table(self, coins, amount):
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



