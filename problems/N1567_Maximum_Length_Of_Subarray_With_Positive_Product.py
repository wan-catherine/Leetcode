class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_zero = -1
        prev_negative = None
        is_even = True
        p_max = 0
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                prev_zero = i
                prev_negative = None
                is_even = True
                res = max(res, p_max)
                p_max = 0
                continue
            if num > 0:
                if is_even:
                    p_max += 1
                else:
                    p_max = max(p_max, i - prev_negative) if prev_negative else max(p_max, i)
            else:
                if prev_negative == None:
                    prev_negative = i
                if is_even:
                    p_max = max(p_max, i - prev_negative)
                else:
                    p_max = i - prev_zero
                is_even = not is_even
            res = max(res, p_max)
        return res

