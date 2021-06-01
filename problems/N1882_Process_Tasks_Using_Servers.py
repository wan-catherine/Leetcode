import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ls, lt = len(servers), len(tasks)
        freepq, busypq = [(servers[i], i) for i in range(ls)], []
        heapq.heapify(freepq)
        res = [None] * lt
        jobs = []
        for i, t in enumerate(tasks):
            heapq.heappush(jobs, i)
            while busypq and busypq[0][0] <= i:
                _, w, idx = heapq.heappop(busypq)
                heapq.heappush(freepq, (w, idx))
            while jobs and freepq:
                job = heapq.heappop(jobs)
                w, idx = heapq.heappop(freepq)
                res[job] = idx
                heapq.heappush(busypq, (i + tasks[job], w, idx))

        while jobs:
            job = heapq.heappop(jobs)
            t, w, idx = heapq.heappop(busypq)
            res[job] = idx
            heapq.heappush(busypq, (t + tasks[job], w, idx))
        return res



