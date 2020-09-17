import collections


class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        start, end = [0,0], [0,0]
        direction = [1,0]
        for i in instructions:
            if i == 'G':
                end[0], end[1] = end[0] + direction[0], end[1] + direction[1]
            elif i == 'L':
                if direction == [1, 0]:
                    direction = [0, -1]
                elif direction == [0, -1]:
                    direction = [-1, 0]
                elif direction == [-1, 0]:
                    direction = [0, 1]
                else:
                    direction = [1, 0]
            else:
                if direction == [1, 0]:
                    direction = [0, 1]
                elif direction == [0, 1]:
                    direction = [-1, 0]
                elif direction == [-1, 0]:
                    direction = [0, -1]
                else:
                    direction = [1, 0]
        if end == start or direction != [1,0]:
            return True
        return False