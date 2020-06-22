import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True
        a = sorted(A)
        length = len(A)
        num_count_mapping = collections.defaultdict(int)
        for i in a:
            num_count_mapping[i] += 1
        for i in range(length-1, -1, -1):
            if not num_count_mapping[a[i]]:
                continue
            if a[i] > 0:
                if a[i] % 2 == 0 and num_count_mapping[a[i] //2] >0:
                    num_count_mapping[a[i]//2] -= 1
                else:
                    return False
            elif a[i] < 0:
                if not num_count_mapping[a[i] * 2]:
                    return False
                else:
                    num_count_mapping[a[i]*2] -= 1
            else:
                if num_count_mapping[0] % 2:
                    return False
                else:
                    num_count_mapping[0] -= 1
            num_count_mapping[a[i]] -= 1
        return True

