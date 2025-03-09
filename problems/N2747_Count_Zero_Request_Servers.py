import collections
from typing import List


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = [(queries[i],i) for i in range(len(queries))]
        queries.sort()
        length = len(logs)
        logs.sort(key=lambda x:x[1])
        cur = collections.deque()
        count = collections.defaultdict(int)
        arr = [0] * len(queries)
        i = 0
        for q, idx in queries:
            l = q - x
            while cur and cur[0][1] < l:
                count[cur[0][0]] -= 1
                if count[cur[0][0]] == 0:
                    del count[cur[0][0]]
                cur.popleft()
            while i < length:
                if logs[i][1] < l:
                    i += 1
                    continue
                if logs[i][1] > q:
                    break
                count[logs[i][0]] += 1
                cur.append(logs[i])
                i += 1
            arr[idx] = n - len(count.keys())
        return arr

    def countServers_20250309(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        lq = len(queries)
        que = [(queries[i], i) for i in range(lq)]
        que.sort(key=lambda x: x[0])
        logs.sort(key=lambda x: x[1])
        pre = collections.defaultdict(int)
        ll = len(logs)
        res = [0] * lq
        i, j = 0, 0
        for q in que:
            t, idx = q
            while j < ll and logs[j][1] <= t:
                pre[logs[j][0]] += 1
                j += 1
            while i < ll and logs[i][1] < t - x:
                pre[logs[i][0]] -= 1
                if pre[logs[i][0]] == 0:
                    del pre[logs[i][0]]
                i += 1
            res[idx] = n - len(pre)
        return res



