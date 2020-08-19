class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(i) for i in str(n)]
        length = len(digits)
        if length == 1:
            return -1

        for i in range(length-1, -1, -1):
            if i > 0 and digits[i] <= digits[i-1]:
                continue
            break
        if i == 0:
            return -1

        j = length - 1
        while j > i:
            if digits[i-1] >= digits[j]:
                j -= 1
                continue
            break
        digits[i-1], digits[j] = digits[j], digits[i-1]
        if i < length - 1:
            new_digits = digits[:i]
            new_digits.extend(sorted(digits[i:]))
            res =  int(''.join([str(i) for i in new_digits]))
        else:
            res = int(''.join([str(i) for i in digits]))
        return res if 2**31 - res > 0 else -1

