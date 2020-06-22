class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        res = []
        up, down, left, right, up_left, up_right, down_left, down_right = 8,8,8,8,8,8,8,8
        for x,y in queens:
            if x == king[0]:
                if y > king[1]:
                    if down == 8 or y-king[1] < down[0]:
                        down = (y - king[1], [x,y])
                else:
                    if up == 8 or king[1]-y < up[0]:
                        up = (king[1]-y, [x,y])
            if y == king[1]:
                if x > king[0]:
                    if right == 8 or x-king[0] < right[0]:
                        right = (x-king[0], [x,y])
                else:
                    if left == 8 or king[0]-x < left[0]:
                        left = (king[0]-x,[x,y])
            if x - king[0] == y - king[1]:
                if x-king[0] > 0:
                    if down_right == 8 or x-king[0] < down_right[0]:
                        down_right = (x-king[0], [x,y])
                else:
                    if up_left == 8 or king[0]-x < up_left[0]:
                        up_left = (king[0]-x,[x,y])
            if x - king[0] == king[1] - y:
                if x-king[0] > 0:
                    if down_left == 8 or x-king[0] < down_left[0]:
                        down_left = (x-king[0], [x,y])
                else:
                    if up_right == 8 or king[0]-x < up_right[0]:
                        up_right = (king[0]-x, [x,y])
        l = [up, down, left, right, up_left, up_right, down_left, down_right]
        for i in l:
            if i != 8:
                res.append(i[1])
        return sorted(res)



