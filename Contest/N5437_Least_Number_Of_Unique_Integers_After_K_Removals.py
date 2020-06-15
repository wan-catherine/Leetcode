import collections


class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if not arr:
            return 0

        num_count_mapping = collections.defaultdict(int)
        for i in arr:
            num_count_mapping[i] += 1

        sorted_list = sorted(num_count_mapping.items(), key = lambda item: item[1])
        for i in range(len(sorted_list)):
            if k > 0 and sorted_list[i][1] > 0:
                if k >= sorted_list[i][1]:
                    k -= sorted_list[i][1]
                    sorted_list[i] = 0
                else:
                    k = 0
            if k == 0:
                break
        count = 0
        for i in range(len(sorted_list)):
            if sorted_list[i] != 0:
                count += 1
        return count
