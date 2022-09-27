import collections
import heapq
import sys
from collections import deque
from math import inf


class Solution(object):
    def findCheapestPrice_dfs_recursive(self, n, flights, src, dst, K):
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

        visited = [0]*n
        ans = self.dfs(src, 0, K, visited, float(inf))
        return -1 if ans == float(inf) else ans

    def dfs(self, src, cost, stops, visited, ans):
        if src == self.dst :
            return cost

        if stops < 0:
            return ans

        for dst_price in self.src_dst_mapping[src]:
            if visited[dst_price[0]]:
                continue
            if cost+dst_price[1] > ans:
                continue
            visited[dst_price[0]] = 1
            ans = self.bfs(dst_price[0], cost+dst_price[1], stops-1, visited, ans)
            visited[dst_price[0]] = 0
        return ans

    def findCheapestPrice_bfs(self, n, flights, src, dst, K):
        src_dst_mapping = collections.defaultdict(list)
        for info in flights:
            src_dst_mapping[info[0]].append((info[1], info[2]))
        ans = float(inf)
        d = deque()
        d.append((src,0))
        while d:
            size = len(d)
            while size:
                cur, cost = d.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for des_price in src_dst_mapping[cur]:
                    if cost + des_price[1] > ans:
                        continue
                    d.append((des_price[0], cost + des_price[1]))
                size -= 1
            K -= 1
            if K < 0:
                break
        return ans if ans != float(inf) else -1


    def findCheapestPrice_wrong_answer(self, n, flights, src, dst, K):
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
    dp[k][c] means : up to kth stops , to city : c , the minimum price .
    dp[k][c] = min(dp[k-1][c], dp[k-1][b] + cost(b,c))
    """
    def findCheapestPrice_dp_two_dimension(self, n, flights, src, dst, K):
        dp = [[float(inf)]*n for _ in range(K+2)]
        dp[0][src] = 0

        for k in range(K+2):
            for flight in flights:
                start = flight[0]
                end = flight[1]
                cost = flight[2]
                dp[k][end] = min(dp[k][end], dp[k-1][start] + cost, dp[k-1][end])
        return dp[K+1][dst] if dp[K+1][dst] != float(inf) else -1

    # update at 20210213
    def findCheapestPrice_dp_one_dimension(self, n, flights, src, dst, K):
        dp = [sys.maxisize] * n
        dp[src] = 0
        for _ in range(K+1):
            prev = dp[:]
            for u, v, w in flights:
                dp[v] = min(dp[v], prev[v], prev[u] + w)
        return dp[dst] if dp[dst] != sys.maxsize else - 1

    # greedy + bfs : Dijkstra's algorithms
    # 20220926 timeout
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(set)
        for u, v, w in flights:
            graph[u].add((v, w))

        stack = [(0, src, 0)]
        memo = {}
        while stack:
            cost, node, step = heapq.heappop(stack)
            if node == dst:
                return cost
            if step == K + 1:
                continue
            for nxt, weight in graph[node]:
                if (nxt, step+1) in memo and memo[(nxt, step+1)] < cost+weight:
                    continue
                memo[(nxt, step+1)] = cost+weight
                heapq.heappush(stack, (cost+weight, nxt, step + 1))
        return -1