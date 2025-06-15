class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        for i, c in enumerate(s):
            if c != '9':
                break
        maximum = 0
        for n in s:
            if n != c:
                maximum = maximum*10 + int(n)
            else:
                maximum = maximum*10 + 9

        for i, c in enumerate(s):
            if c > '1':
                break
        if i == 0 or (i == len(s) - 1 and s[i] == '1'):
            replace = 1
        else:
            replace = 0
        minimum = 0
        for n in s:
            if n != c:
                minimum = minimum * 10 + int(n)
            else:
                minimum = minimum *10 + replace
        return maximum - minimum

    def maxDiff_20250615(self, num: int) -> int:
        snum = str(num)
        length = len(snum)
        xarr, yarr = [snum[0]], [snum[0]]
        for i in range(1, length):
            if snum[i] not in xarr:
                xarr.append(snum[i])
        for i in range(1, length):
            if snum[i] not in yarr:
                yarr.append(snum[i])
        if len(xarr) == 1:
            return int('8' * length)
        x = '9'
        for c in xarr:
            if x != c:
                x = c
                break
        if yarr[0] != '1':
            y = yarr[0]
            ry = '1'
        else:
            i = 1
            while i < len(yarr) and yarr[i] == '0':
                i += 1
            if i == len(yarr):
                y = yarr[1]
                ry = '0'
            else:
                y = yarr[i]
                ry = '0'
        a, b = [], []
        for i in range(length):
            if snum[i] == x:
                a.append('9')
            else:
                a.append(snum[i])
        for i in range(length):
            if snum[i] == y:
                b.append(ry)
            else:
                b.append(snum[i])
        return int(''.join(a)) - int(''.join(b))