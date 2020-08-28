class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        length = len(S)
        l = min(11, length) # each integer fits a 32-bit signed integer type, so the largest integer is 2147483648 which is 10 length.
        for f_len in range(1, l):
            for s_len in range(1, l):
                res = [int(S[:f_len])]
                if self.check(f_len, s_len, S, res):
                    return res
        return []

    def check(self, f_len, s_len, s, res):
        first = int(s[:f_len])
        if len(str(first)) < f_len or first > 2**31:
            return False
        second = int(s[f_len:f_len+s_len])
        if len(str(second)) < s_len or second > 2 **31:
            return False
        res.append(second)
        next = first + second
        next_str = str(next)
        n_len = len(next_str)
        next_index = f_len+s_len+n_len
        if next_index > len(s):
            return False
        if s[f_len+s_len:f_len+s_len+n_len] != next_str or next > 2**31:
            return False
        if next_index == len(s):
            res.append(next)
            return True
        return self.check(s_len,n_len,s[f_len:], res)

