from math import inf
from typing import List


class Solution(object):
    def shoppingOffers_(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.memo = {tuple([0]*len(needs)):0}

        self.helper(price, special, needs)
        # print(self.memo)
        return self.memo[tuple(needs)]

    def helper(self, price, special, needs):
        key = tuple(needs)
        if key in self.memo:
            return self.memo[key]
        value = float(inf)
        for li in special:
            temp = needs[:]
            flag = True
            for index, val in enumerate(needs):
                if li[index] > val:
                    flag = False
                    break
                temp[index] -= li[index]
            if flag:
                value = min(value, self.helper(price, special, temp) + li[-1])

        # if I use this part of code, it will be TLE.
        # Actually, we don't need to do recursive for normal price.If there is some status can't use any special,
        # it will be covered by calculating all cost .
        # for index, p in enumerate(price):
        #     temp = needs[:]
        #     if needs[index] > 0:
        #         temp[index] -= 1
        #         value = min(value, self.helper(price, special, temp) + p)

        cost = 0
        for index, val in enumerate(needs):
            cost += val * price[index]
        value = min(value, cost)
        self.memo[key] = value
        return value

    """
    update : 20210401
    """
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        lp = len(price)
        needs = tuple(needs)
        memo = {}
        def dfs(state):
            nonlocal lp
            if state in memo:
                return memo[state]
            if sum(state) == 0:
                return 0
            temp = list(state)
            val = sum(price[i]*state[i] for i in range(lp))
            for li in special:
                for i in range(lp):
                    if temp[i] < li[i]:
                        temp = list(state)  # here need to recover temp !!!
                        break
                    else:
                        temp[i] -= li[i]
                else:
                    val = min(val, dfs(tuple(temp)) + li[-1])
                    temp = list(state)
                # new_state = [state[i] - li[i] for i in range(lp)]
                # if min(new_state) >= 0:
                #     val = min(val, dfs(tuple(new_state)) + li[-1])
            memo[(state)] = val
            return val

        res = dfs(tuple(needs))
        # print(memo)
        return res
