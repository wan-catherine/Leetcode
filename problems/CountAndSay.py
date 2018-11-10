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