class Solution:
    def nthUglyNumber_before(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        info2, info3, info5 = 2,3,5

        i2=i3=i5=0
        res = [1]
        while i < n:
            if info2 == res[-1]:
                i2 +=1
                info2 = res[i2] * 2
            if info3 == res[-1]:
                i3 +=1
                info3 = res[i3] * 3
            if info5 == res[-1]:
                i5 +=1
                info5 = res[i5] * 5

            temp = min(info2, info3, info5)
            res.append(temp)
            i += 1
            if temp == info2:
                i2 += 1
                info2 = res[i2] * 2
            elif temp == info3:
                i3 += 1
                info3 = res[i3] * 3
            elif temp == info5:
                i5 += 1
                info5 = res[i5] * 5
        return res[-1]

    """
    res = [ ...a...b,b1,..c... ] , so for next ugly number X
    It can be X = min(a*2, b*3, c*5)
    Let's say X = b*3
    Then for next next ugly number Y 
    Y = min(a*2, b1*3, c*5)
    Here b1 is the ugly number after b
    """
    def nthUglyNumber(self, n):
        res = [1]
        i_2, i_3, i_5 = 0, 0, 0
        for i in range(1, n):
            num = min(res[i_2]*2, res[i_3]*3, res[i_5]*5)
            if num == res[i_2] * 2:
                i_2 += 1
            if num == res[i_3] * 3:
                i_3 += 1
            if num == res[i_5] * 5:
                i_5 += 1
            res.append(num)
        return res[-1]






