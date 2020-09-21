import collections


class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(targetGrid), len(targetGrid[0])
        color_pos = [[rows, cols, 0, 0] for _ in range(61)]
        colors = set()
        for i in range(rows):
            for j in range(cols):
                c = targetGrid[i][j]
                colors.add(c)
                color_pos[c][0] = min(color_pos[c][0], i)
                color_pos[c][1] = min(color_pos[c][1], j)
                color_pos[c][2] = max(color_pos[c][2], i)
                color_pos[c][3] = max(color_pos[c][3], j)

        def test(c):
            for i in range(color_pos[c][0], color_pos[c][2]+1):
                for j in range(color_pos[c][1], color_pos[c][3]+1):
                    if targetGrid[i][j] > 0 and targetGrid[i][j] != c:
                        return False
            for i in range(color_pos[c][0], color_pos[c][2]+1):
                for j in range(color_pos[c][1], color_pos[c][3]+1):
                    targetGrid[i][j] = 0
            return True

        """
        First, I checked from the number of colors. Then it failed at test_isPrintable_5. It checked 1 before 3. 
        Here, it uses while to check all colors . 
        """
        while colors:
            new_color = set()
            for i in colors:
                if not test(i):
                    new_color.add(i)
            if len(new_color) == len(colors):
                return False
            colors = new_color
        return True