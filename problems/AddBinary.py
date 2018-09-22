class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        l = la if la > lb else lb
        flag = 0
        res = []
        for i in range(l):
            n = flag
            if i < la :
                n += int(a[la - i - 1])
            if i < lb:
                n += int(b[lb - i - 1])
            if n > 1:
                flag = 1
            else:
                flag = 0
            res.append(n%2)
        if flag > 0:
            res.append(flag)
        return ''.join(str(e) for e in res[::-1])