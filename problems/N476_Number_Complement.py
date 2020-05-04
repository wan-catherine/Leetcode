class Solution:
    def findComplement_1(self, num: int) -> int:
        res = []
        while num >= 0:
            i = 0
            while 2 ** i <= num:
                i += 1
            res.append(i - 1)
            num -= 2 ** (i - 1)
        s = 0
        for i in range(1, len(res)):
            for j in range(res[i] + 1, res[i-1]):
                s += 2 ** j
        return s

    def findComplement(self, num: int) -> int:
        lst1 = []
        while (num != 0):
            lst1.append(num % 2)
            num = num // 2
        n = len(lst1)
        sum1 = 0
        for i in range(n):
            if (lst1[i] == 0):
                sum1 += pow(2, i)
        return sum1