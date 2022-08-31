from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        sb = set((r, c) for r, c in blocked)
        # print(sb)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def check(x, y):
            visited = set()
            visited.add((x, y))
            stack = [(x, y)]
            while stack and len(visited) < 20000:
                nstack = []
                for r, c in stack:
                    for i, j in directions:
                        row, col = r + i, c + j
                        if row < 0 or row >= 10 ** 6 or col < 0 or col >= 10 ** 6:
                            continue
                        if (row, col) in visited or (row, col) in sb:
                            continue
                        if row == target[0] and col == target[1]:
                            return 0
                        visited.add((row, col))
                        nstack.append((row, col))
                stack = nstack
            return 1 if stack else -1

        if not blocked:
            return True

        s, t = check(*source), check(*target)
        # print(s, t)
        if s == 0 or t == 0:
            return True
        if s == 1 and t == 1:
            return True
        return False
