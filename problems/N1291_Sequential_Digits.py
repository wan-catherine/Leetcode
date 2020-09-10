class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        l, h = str(low), str(high)
        nums = "123456789"
        length = len(l) - 1
        res = []
        for i in range(len(h) - len(l) + 1):
            length += 1
            start, end = 0, length
            while end <= 9:
                num = int(nums[start:end])
                if num < low:
                    start += 1
                    end += 1
                    continue
                if num > high:
                    break
                res.append(num)
                start += 1
                end += 1
        return res
