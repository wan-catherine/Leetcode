class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        rows, cols = len(seats), len(seats[0])
        times = 1 << cols
        state = [0] * times
        self_ok_memo, cross_ok_memo = {}, {}

        def is_self_ok(pattern, row):
            if (pattern, row) in self_ok_memo:
                return self_ok_memo[(pattern, row)]
            nonlocal cols
            li = []
            p = pattern
            for i in range(cols):
                li.append(p % 2)
                p //= 2
            res = True
            for i in range(cols):
                if not li[i]:
                    continue
                elif seats[row][i] == '#':
                    res = False
                elif i > 0 and li[i - 1]:
                    res = False
                elif i < cols - 1 and li[i + 1]:
                    res = False
            self_ok_memo[(pattern, row)] = res
            return res

        def is_cross_ok(cur, prev):
            if (cur, prev) in cross_ok_memo:
                return cross_ok_memo[(cur, prev)]

            nonlocal cols
            li_cur, li_prev = [], []
            for i in range(cols):
                li_cur.append(cur % 2)
                cur //= 2
                li_prev.append(prev % 2)
                prev //= 2
            res = True
            for i in range(cols):
                if not li_cur[i]:
                    continue
                if i > 0 and li_prev[i - 1]:
                    res = False
                elif i < cols - 1 and li_prev[i + 1]:
                    res = False
            cross_ok_memo[(cur, prev)] = res
            return res

        def count(pattern):
            res = 0
            while pattern:
                res += pattern % 2
                pattern //= 2
            return res

        for p in range(times):
            if is_self_ok(p, 0):
                state[p] = count(p)

        for row in range(1, rows):
            old_state = state[:]
            for cur in range(times):
                state[cur] = 0
                if not is_self_ok(cur, row):
                    continue
                for prev in range(times):
                    if not is_self_ok(prev, row - 1):
                        continue
                    if not is_cross_ok(cur, prev):
                        continue
                    state[cur] = max(state[cur], old_state[prev] + count(cur))
        return max(state)