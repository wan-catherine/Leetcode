class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        before = "11"
        for i in range(2, n):
            j = 1
            count = 1
            temp = ""
            while j < len(before):
                if before[j] == before[j - 1]:
                    count += 1
                else:
                    temp += str(count) + str(before[j-1])
                    count = 1
                j += 1
            else:
                temp += str(count) + str(before[-1])
            before = temp
        return before

    def countAndSay(self, n: int) -> str:
        cur = "1"
        while n - 1:
            l = len(cur)
            ncur = ''
            i = 0
            while i < l:
                j = i
                while j < l and cur[j] == cur[i]:
                    j += 1
                ncur += '{}{}'.format(j - i, cur[i])
                i = j
            cur = ncur
            n -= 1
        return cur