class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        num_dict = {}
        for li in intervals:
            if li[0] not in num_dict:
                num_dict[li[0]] = li[1]
            elif li[1] > num_dict[li[0]]:
                num_dict[li[0]] = li[1]

        sorted_key = sorted(num_dict)
        if not sorted_key:
            return []
        cur_key = sorted_key[0]
        res = []
        for key in sorted_key[1:]:
            if key > num_dict[cur_key]:
                res.append([cur_key, num_dict[cur_key]])
                cur_key = key
            elif num_dict[cur_key] < num_dict[key]:
               num_dict[cur_key] = num_dict[key]
        res.append([cur_key, num_dict[cur_key]])
        return res



