class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ""
        length = len(s)
        k = 2 * numRows - 2
        if k < 1:
            k = numRows

        for i in range(numRows):
            multiple = 0
            index = 0

            if i == 0 or i == numRows -1 :
                while index < length:
                    index = multiple * k + i
                    if index < length:
                        print(s[index])
                        res += s[index]
                    multiple += 1
            else:
                while index < length - 1:
                    q1 = multiple * k - i
                    q2 = multiple * k + i
                    if -1 < q1 < length:
                        res += s[q1]
                        print(s[q1])
                    if q2 < length:
                        res += s[q2]
                        print(s[q2])
                    index = q2
                    multiple += 1

        return res
