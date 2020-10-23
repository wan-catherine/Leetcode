class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        if x_center >= x1 and x_center <= x2 and y_center >= y1 and y_center <= y2:
            return True

        if x_center < x1 and y_center > y2:
            x, y = x1, y2
        elif x_center >= x1 and x_center <= x2 and y_center > y2:
            x, y = x_center, y2
        elif x_center > x2 and y_center > y2:
            x, y = x2, y2
        elif x_center < x1 and y_center <= y2 and y_center >= y1:
            x, y = x1, y_center
        elif x_center > x2 and y_center <= y2 and y_center >= y1:
            x, y = x2, y_center
        elif x_center < x1 and y_center < y1:
            x, y = x1, y1
        elif x_center <= x2 and x_center >= x1 and y_center < y1:
            x, y = x_center, y1
        elif x_center > x2 and y_center< y1:
            x, y = x2, y1

        if (x-x_center)*(x-x_center) + (y-y_center)*(y-y_center) <= radius*radius:
            return True
        else:
            return False