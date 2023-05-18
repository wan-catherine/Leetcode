import heapq
from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        length = len(reward1)
        pq = []
        for i in range(length):
            heapq.heappush(pq, (reward2[i] - reward1[i], i))

        arr = [False] * length

        while k:
            diff, idx = heapq.heappop(pq)
            arr[idx] = True
            k -= 1

        res = 0
        for i in range(length):
            if arr[i]:
                res += reward1[i]
            else:
                res += reward2[i]
        return res