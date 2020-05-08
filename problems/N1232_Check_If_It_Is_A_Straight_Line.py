class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if not coordinates or len(coordinates) < 2:
            return False

        base_point = coordinates[0]
        if coordinates[1][0] - base_point[0] == 0:
            return False
        slope = (coordinates[1][1] - base_point[1]) / (coordinates[1][0] - base_point[0])
        for i in range(2, len(coordinates)):
            if coordinates[i][0] -base_point[0] == 0:
                return False
            if slope != (coordinates[i][1] - base_point[1])/(coordinates[i][0] -base_point[0]):
                return False

        return True