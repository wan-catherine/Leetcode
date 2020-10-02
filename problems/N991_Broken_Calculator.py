class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y

        res = 0
        while Y > X:
            if Y%2:
                res += 1
                Y = (Y+1) // 2
            else:
                Y = Y // 2
            res += 1
        return res + X - Y

