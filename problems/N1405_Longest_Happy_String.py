class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        a1,b1,c1 = 0, 0, 0
        res = []
        while a >= 0 or b >= 0 or c >= 0:
            if a >= b and a >= c:
                while a1 < 2 and a > 0:
                    res.append('a')
                    b1,c1 = 0, 0
                    a1+=1
                    a -= 1
                else:
                    if b >= c and b > 0:
                        res.append('b')
                        b1 += 1
                        b -= 1
                        a1,c1 = 0, 0
                    elif c >= b and c > 0:
                        res.append('c')
                        c1+=1
                        c -= 1
                        a1,b1 = 0, 0
                    else:
                        break
            elif b >= a and b >= c:
                while b1 < 2 and b > 0:
                    res.append('b')
                    a1,c1 = 0, 0
                    b1+= 1
                    b -= 1
                else:
                    if a >= c and a > 0:
                        res.append('a')
                        a1+=1
                        a-=1
                        b1,c1 = 0,0
                    elif c >= a and c > 0:
                        res.append('c')
                        c1+=1
                        c -= 1
                        a1, b1 = 0,0
                    else:
                        break
            elif c >= a and c >= b:
                while c1 < 2 and c > 0:
                    res.append('c')
                    c -= 1
                    c1 += 1
                    a1, b1 = 0, 0
                else:
                    if a >= b and a > 0:
                        res.append('a')
                        a -= 1
                        a1 += 1
                        b1,c1 = 0, 0
                    elif b >= a and b > 0:
                        res.append('b')
                        b -= 1
                        b1 += 1
                        a1,c1 = 0, 0
                    else:
                        break
        return ''.join(res)

