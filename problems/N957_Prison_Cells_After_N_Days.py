class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        status = set()
        count = 0
        has_cycle = False
        i = 0
        while i < N:
            cur = self.next_day(cells)
            key = ''.join(map(str,cur))
            if key not in status:
                status.add(key)
                count += 1
            else:
                has_cycle = True
                break
            i += 1
            cells = cur # make cells is the last one of the cycle , so then next_day(cells) will enter the cycle
            print(cur)
        if has_cycle:
            N %= count
            for i in range(0, N):
                cells = self.next_day(cells)
        return cells

    def next_day(self, cells):
        next = [0] * 8
        for i in range(1, 7):
            next[i] = 0 if cells[i-1] != cells[i+1] else 1
        return next

