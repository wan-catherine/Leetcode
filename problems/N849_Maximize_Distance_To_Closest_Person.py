class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = 1
        arr = []
        for i, v in enumerate(seats):
            if v == 1:
                arr.append(i)

        for s, e in zip(arr, arr[1:]):
            l = (e - s) // 2
            res = max(res, l)
        res = max(res, arr[0], len(seats) - 1 - arr[-1])
        return res

