import bisect
import collections
from typing import List


class Solution:
    def closestRoom_TLE(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: x[1], reverse=True)
        mapping = {}
        ps, previous, keys = 0, [], []
        for id, size in rooms:
            if size != ps:
                mapping[size] = previous[:]
                bisect.insort_left(keys, size)
            bisect.insort_left(mapping[size], id)
            ps, previous = size, mapping[size]
        res = []
        # keys = sorted(mapping.keys())
        for pre, ms in queries:
            ik = bisect.bisect_left(keys, ms)
            if ik >= len(keys):
                res.append(-1)
                continue
            key = keys[ik]
            index = bisect.bisect_left(mapping[key], pre)
            if index < len(mapping[key]):
                gap = abs(mapping[key][index] - pre)
                ans = index
                if index < len(mapping[key]) - 1:
                    if abs(mapping[key][index + 1] - pre) < gap:
                        gap = abs(mapping[key][index + 1] - pre)
                        ans = index + 1
                if index > 0:
                    if abs(mapping[key][index - 1] - pre) <= gap:
                        gap = abs(mapping[key][index - 1] - pre)
                        ans = index - 1
                res.append(mapping[key][ans])
            else:
                res.append(mapping[key][-1])
        return res

    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: -x[1])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x : x[1], reverse=True)
        cur, ids = 0, []
        res = [-1] * len(queries)
        for pre, msize, pos in queries:
            while cur < len(rooms) and rooms[cur][1] >= msize:
                bisect.insort_left(ids, rooms[cur][0])
                cur += 1
            if not ids:
                continue
            index = bisect.bisect_left(ids, pre)
            if index >= len(ids):
                res[pos] = ids[-1]
                continue
            gap, ans = abs(ids[index] - pre), ids[index]
            if index < len(ids) - 1:
                if abs(ids[index+1] - pre) < gap:
                    gap = abs(ids[index+1] - pre)
                    ans = ids[index+1]
            if index > 0:
                if abs(ids[index-1] - pre) <= gap:
                    ans = ids[index-1]
            res[pos] = ans
        return res