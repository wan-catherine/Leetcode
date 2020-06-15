import collections
from math import inf


class Solution(object):
    def findCheapestPrice_timeout(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        self.dst = dst
        self.src_dst_mapping = collections.defaultdict(list)
        for info in flights:
            self.src_dst_mapping[info[0]].append((info[1], info[2]))

        return self.bfs(src, -1, K)

    def bfs(self, src, price, stops):
        if src not in self.src_dst_mapping or stops < 0:
            return -1

        minimum = 10001

        for dst_price in self.src_dst_mapping[src]:
            if self.dst == dst_price[0]:
                temp_price = dst_price[1] if price == -1 else price+dst_price[1]
            else:
                next_price = self.bfs(dst_price[0], dst_price[1], stops-1)
                if next_price == -1:
                    temp_price = -1
                else:
                    temp_price = price + next_price if price > -1 else next_price
            if temp_price > -1:
                minimum = min(temp_price, minimum)

        return -1 if minimum == 10001 else minimum

    def findCheapestPrice(self, n, flights, src, dst, K):
        d_base = [[float(inf)] * n for _ in range(n)]
        for i in range(n):
            d_base[i][i] = 0
        for info in flights:
            d_base[info[0]][info[1]] = info[2]

        for _ in range(K+1):
            for i in range(n):
                d_new = [[float(inf)] * n for _ in range(n)]
                for j in range(n):
                    d_new[j][j] = 0
                    d_new[i][j] = d_base[i][j]
                    d_new[j][i] = d_base[j][i]

                for row in range(n):
                    if row == i:
                        continue
                    for col in range(n):
                        if col == i:
                            continue
                        base = d_base[row][col]
                        new = d_base[row][i] + d_base[i][col]
                        d_new[row][col] = min(base, new)

                d_base = d_new
        if d_new[src][dst] == float(inf):
            return  -1
        else:
            return d_new[src][dst]

    """
    Floyd Warshar Algorithm
    Because we already know src, so dp[i] means minimum price from src - i .
    The ourside loop use stops K. 
    dp[info[1]] = min(dp[info[1]], dp_temp[info[0]] + info[2])
    when it needs to stop, then use last time dp_temp, it means this loop (k) update
    when it doesn't need to stop , then use the current time dp.
    """
    def findCheapestPrice_other(self, n, flights, src, dst, K):
        dp = [float(inf)] * n
        dp[src] = 0
        for i in range(K+1):
            dp_temp = dp[:]
            for info in flights:
                dp[info[1]] = min(dp[info[1]], dp_temp[info[0]] + info[2])
        if dp[dst] == float(inf):
            return -1
        else:
            return dp[dst]
