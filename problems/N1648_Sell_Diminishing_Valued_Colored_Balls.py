import collections
import math


class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        res = 0
        inventory.sort()

        total = sum(inventory)
        length = len(inventory)
        i = 0
        while inventory[i] * (length - i) < total - orders:
            total -= inventory[i]
            i += 1

        left = (total - orders) // (length - i) + 1 # add one here in order to avoid orders < 0.
        for j in range(i, length):
            res += (inventory[j] + left + 1) * (inventory[j] - left) // 2
            orders -= (inventory[j] - left)

        # so here order is among [0, length-i)
        while orders:
            res += left
            orders -= 1

        return res % mod


