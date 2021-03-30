class Solution(object):
    def canIWin_(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= maxChoosableInteger:
            return True
        max_sum = sum([i for i in range(1, maxChoosableInteger+1)])
        if max_sum < desiredTotal:
            return False

        self.maximum = maxChoosableInteger
        self.status = [0] * (2**maxChoosableInteger)
        return self.dfs(desiredTotal, 0)

    def dfs(self, total, state):
        if total <= 0:
            return False
        if self.status[state]:
            return self.status[state] == 1
        for i in range(self.maximum):
            if state & (1 << i):
                continue
            # if the next player can't win, then I win. There might be a lot of ways, if there is a way to win, then this is the optical choose.
            if not self.dfs(total - i - 1, state | (1 << i)):
                self.status[state] = 1
                return True
        self.status[state] = -1
        return False

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # need to check this, or it will fail for (5, 50)
        max_sum = sum([i for i in range(1, maxChoosableInteger + 1)])
        if max_sum < desiredTotal:
            return False

        memo = {}

        def dfs(state, cur):
            nonlocal desiredTotal
            # for (5, 50), it will return True.so need to check before do dfs
            if cur >= desiredTotal:
                return True
            if (state, cur) in memo:
                return memo[(state, cur)]
            flag = False
            for i in range(1, maxChoosableInteger + 1):
                if state & (1 << i):
                    continue
                if dfs(state | (1 << i), cur + i):
                    flag = True
                    break
            memo[(state, cur)] = not flag
            return not flag

        for i in range(1, maxChoosableInteger + 1):
            if dfs(0 | (1 << i), i):
                return True
        return False


