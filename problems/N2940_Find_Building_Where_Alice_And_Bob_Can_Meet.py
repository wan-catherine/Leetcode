import bisect
from collections import deque
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        length = len(heights)
        lq = len(queries)
        ql = [(min(queries[i]), max(queries[i]), i) for i in range(lq)]
        ql.sort(key=lambda x: -x[1])
        res = [-1] * lq
        stack = deque()
        i = length - 1
        for a, b, idx in ql:
            while i >= b:
                while stack and stack[0][0] <= heights[i]:
                    stack.popleft()
                stack.appendleft((heights[i], i))
                i -= 1
            if heights[a] < heights[b] or a == b:
                res[idx] = b
                continue
            # here max(heights[b], heights[a]) + 1, because If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j]
            j = bisect.bisect_left(stack, (max(heights[b], heights[a]) + 1, b))
            if j == len(stack):
                res[idx] = -1
            else:
                res[idx] = stack[j][1]
        return res

