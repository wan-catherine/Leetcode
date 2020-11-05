class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        v, h = destination
        n = v + h
        res = []

        def combinartion_count(n, k):
            count = 1
            for i in range(1, k+1):
                count *= (n - i + 1)
                count //= i
            return count

        for i in range(n):
            if not h:
                res.append('V')
                v -= 1
                continue
            elif not v:
                res.append('H')
                h -= 1
                continue

            count = combinartion_count(h+v-1, v)
            if k <= count:
                res.append('H')
                h -= 1
            else:
                k -= count
                res.append('V')
                v -= 1
        return ''.join(res)


