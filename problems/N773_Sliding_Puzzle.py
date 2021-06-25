from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board[0].extend(board[1])
        stack = [board[0]]
        target = [1,2,3,4,5,0]
        memo = set()
        memo.add(tuple(stack[0]))
        step = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            new_stack = []
            for bd in stack:
                if bd == target:
                    return step
                for idx in range(6):
                    if bd[idx] == 0:
                        break
                r, c = idx // 3, idx % 3
                for i, j in directions:
                    row, col = r + i, c + j
                    if row < 0 or row >= 2 or col < 0 or col >= 3:
                        continue
                    index = row * 3 + col
                    li = bd[:]
                    li[idx], li[index] = li[index], li[idx]
                    if tuple(li) in memo:
                        continue
                    memo.add(tuple(li))
                    new_stack.append(li)
            stack = new_stack
            step += 1
        return -1

