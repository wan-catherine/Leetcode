class Solution(object):
    def countBits_(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0, 1] + [0] * (num - 1)
        if num < 2:
            return res[:num + 1]

        i = 1
        j = 2
        while True:
            start = 2 ** i
            if j > num:
                break
            while j < start * 2 :
                if j > num:
                    break
                k = j - start
                res[j] = res[k] + 1
                j += 1
            if j <= num and j == start * 2:
                res[j] = 1
                i += 1
                j += 1
        return res

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        lst = [0] * (num + 1)
        for i in range(1, num + 1):
            lst[i] = lst[i & (i - 1)] + 1
        return lst
