from typing import List

from sortedcontainers import SortedList


class Solution:
    def maximumSegmentSum_slow(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        length = len(nums)
        prev = [0]
        for i in range(length):
            prev.append(prev[-1] + nums[i])
        segments, sums = SortedList(), SortedList([0])

        def add(l, r):
            segments.add((l, r))
            sums.add(prev[r+1] - prev[l])

        def remove(l, r):
            segments.remove((l, r))
            sums.remove((prev[r+1] - prev[l]))
        res = []
        add(0, length-1)
        for i in removeQueries:
            # this is the key part . need to search i+1, then move previous index
            idx = segments.bisect_left((i+1, -1)) - 1
            left, right = segments[idx]

            remove(left, right)
            if left != i:
                add(left, i -1)
            if i != right:
                add(i+1, right)
            res.append(sums[-1])
        return res

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        mapping, cur, res = {}, 0, []
        # here we don't include the first element in removeQueries.
        for i in reversed(removeQueries[1:]):
            mapping[i] = (nums[i], 1)
            rv, rl = mapping.get(i+1, (0,0))
            lv, ll = mapping.get(i-1, (0,0))
            total = nums[i] + rv + lv
            length = rl + ll + 1
            mapping[i+rl] = (total, length)
            mapping[i-ll] = (total, length)
            cur = max(cur, total)
            res.append(cur)
        return res[::-1] + [0]


