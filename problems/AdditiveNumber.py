class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num == None or len(num) < 3:
            return False
        l = len(num)
        i = 1
        while i <= l // 2:
            j = 1
            if i > 1 and num[0] == '0':
                return False
            first = int(num[0:i])
            while l - i - j >= max(i, j):
                if num[i] == '0' and j > 1:
                    break

                second = int(num[i: i+ j])
                if self.isValid(first, second, i+j, num):
                    return True
                j += 1
            i += 1
        return False

    def isValid(self, first, second, start, num):
        if start == len(num):
            return True

        second += first
        first = second - first
        sum = str(second)
        return num.startswith(sum, start) and self.isValid(first, second, start+len(sum), num)
