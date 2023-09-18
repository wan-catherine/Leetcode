from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        length = len(positions)
        mp = []
        for i in range(length):
            mp.append([positions[i], i])
        mp.sort()
        stack = []
        for _, i in mp:
            flag = True
            while stack and stack[-1][1] == 'R' and directions[i] == 'L':
                if healths[i] == stack[-1][0]:
                    stack.pop()
                    flag = False
                    break
                if healths[i] < stack[-1][0]:
                    stack[-1][0] -= 1
                    flag = False
                    break
                healths[i] -= 1
                stack.pop()
            if flag:
                stack.append([healths[i], directions[i], i])
        stack.sort(key=lambda x: x[2])
        return [i for [i, _, _] in stack]