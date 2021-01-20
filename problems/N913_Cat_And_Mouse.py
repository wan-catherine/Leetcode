from collections import deque


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        length = len(graph)
        status = [[[0]*3 for _ in range(length)] for _ in range(length)]
        queue = deque()
        for i in range(1, length):
            for t in range(1, 3):
                status[i][i][t] = 2
                queue.append((i, i, t))
                status[0][i][t] = 1
                queue.append((0, i, t))

        def find_prev_status(m, c, t):
            res = []
            if t == 1:
                for prev in graph[c]:
                    if prev == 0:
                        continue
                    res.append((m, prev, 2))
            else:
                for prev in graph[m]:
                    res.append((prev, c, 1))
            return res

        def is_all_next_win(m, c, t):
            if t == 1:
                for nm in graph[m]:
                    if status[nm][c][2] != 2:
                        return False
            else:
                for nc in graph[c]:
                    if nc == 0:
                        continue
                    if status[m][nc][1] != 1:
                        return False
            return True

        while queue:
            m, c, t = queue.popleft()
            current = status[m][c][t]
            for pm, pc, pt in find_prev_status(m, c, t):
                if status[pm][pc][pt] != 0:
                    continue
                # current is mouse win and cat turn, so previous is mouse turn, so it definitely will choose to go this way to get current
                if current == 1 and t == 2 :
                    status[pm][pc][pt] = 1
                    queue.append((pm, pc, pt))
                # current is cat win and mouse turn, so previous is cat turn, so it definitely will choose to go this way to get current
                elif current == 2 and t == 1:
                    status[pm][pc][pt] = 2
                    queue.append((pm, pc, pt))
                # if all the next move of this previous all win , then this previous is forced to be lose
                elif is_all_next_win(pm, pc, pt):
                    status[pm][pc][pt] = 3 - pt
                    queue.append((pm, pc, pt))

        return status[1][2][1]
