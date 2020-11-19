from functools import lru_cache
"""
Classical matrix dp problem. From left_up to right to down. 

The key point is how to maintain the left and up status. 
Here we maintain the last row state instead of main the whole matrix. 
We maintain last_row_state , so the up is last_row_state[col], the left is last_row_state[col-1]. 
And it's much easier to be key in the memo.
If we use a matrix, it will be more complicated. 
"""

class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        def get_happiness(col, person, last_row_state):
            up = last_row_state[col]
            left = last_row_state[col-1] if col > 0 else None

            res = 0
            if up == 1:
                res -= 30
            elif up == 2:
                res += 20

            if left == 1:
                res -= 30
            elif left == 2:
                res += 20

            neighbors = (1 if up else 0) + (1 if left else 0)
            if person == 1:
                res += 120 - 30 * neighbors
            elif person == 2:
                res += 40 + 20 * neighbors
            return res

        @lru_cache(None)
        def dp(index, intro, extro, last_row_state):
            if index == m * n:
                return 0

            col = index % n

            list_last_row_state = list(last_row_state)
            old_val = list_last_row_state[col]

            # don't place any person : 0
            list_last_row_state[col] = 0
            ans = dp(index+1, intro, extro, tuple(list_last_row_state))
            list_last_row_state[col] = old_val

            # place an introvert person : 1
            if intro:
                happiness = get_happiness(col, 1, list_last_row_state)
                list_last_row_state[col] = 1
                ans = max(ans, dp(index+1, intro-1, extro, tuple(list_last_row_state)) + happiness)
                list_last_row_state[col] = old_val

            # place an extrovert person : 2
            if extro:
                happiness = get_happiness(col, 2, list_last_row_state)
                list_last_row_state[col] = 2
                ans = max(ans, dp(index + 1, intro, extro - 1, tuple(list_last_row_state)) + happiness)
                list_last_row_state[col] = old_val

            return ans
        return dp(0, introvertsCount, extrovertsCount, tuple([0]*n))