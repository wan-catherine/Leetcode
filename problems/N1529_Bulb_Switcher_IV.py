class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        is_odd = False
        count = 0
        # length = len(target)
        # start = 0
        # while start < length:
        #     if target[start] == '0':
        #         if is_odd:
        #             count += 1
        #             is_odd = not is_odd
        #     else:
        #         if not is_odd:
        #             count += 1
        #             is_odd = not is_odd
        #     start += 1
        # return count

        for s in target:
            if (s == '0' and is_odd) or (s == '1' and not is_odd):
                count += 1
                is_odd = not is_odd
        return count

