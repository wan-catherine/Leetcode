class Solution(object):
    def nextGreaterElement_(self, n):
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

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        chars = []
        while n:
            chars.append(n % 10)
            n //= 10
        if sorted(chars) == chars:
            return -1
        length = len(chars)

        def helper(idx):
            for i in range(idx + 1, length):
                if chars[i] < chars[idx]:
                    return i
            return length

        index = length
        res = [None, None]
        for i in range(length):
            if i >= index:
                break
            idx = helper(i)
            if idx >= length:
                continue
            else:
                # we only update res when it's none or larger.
                # see test_nextGreaterElement_3
                if (res[1] and res[1] > idx) or not res[1]:
                    res = [i, idx]
                    index = min(index, idx)
        chars[res[0]], chars[res[1]] = chars[res[1]], chars[res[0]]
        chars = sorted(chars[:res[1]], reverse=True) + chars[res[1]:]
        num = int(''.join(str(i) for i in chars[::-1]))
        if num > 2 ** 31:
            return -1
        return num

