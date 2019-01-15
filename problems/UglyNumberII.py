class Solution:
    def nthUglyNumber(self, n):
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



