import bisect


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        length = len(num)
        def helper(ns):
            i = length - 1
            cur = [int(ns[i])]
            while i > 0 and ns[i] <= ns[i-1]:
                bisect.insort_left(cur, int(ns[i-1]))
                i -= 1
            v = int(ns[i-1])
            idx = bisect.bisect_right(cur, v)
            v, cur[idx] = cur[idx], v
            cur.sort()
            res = ns[:i-1] + str(v) + ''.join(str(i) for i in cur)
            return res

        cur = num
        while k:
            cur = helper(cur)
            k -= 1

        res = 0
        li = list(num)
        for i in range(length):
            ans = 0
            for j in range(length):
                if li[j] == '#':
                    continue
                if li[j] == cur[i]:
                    li[j] = '#'
                    break
                ans += 1
            res += ans
        return res
