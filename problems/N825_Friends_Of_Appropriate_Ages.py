import collections


class Solution(object):
    def numFriendRequests_n_n(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # age_count_mapping = collections.defaultdict(int)
        # for age in ages:
        #     age_count_mapping[age] += 1
        age_count_mapping = collections.Counter(ages)
        res = 0
        for a in age_count_mapping:
            for b in age_count_mapping:
                if not self.can_request(a, b):
                    continue
                if a == b:
                    res += age_count_mapping[a] * (age_count_mapping[a] - 1)
                else:
                    res += age_count_mapping[a] * age_count_mapping[b]
        return res


    def can_request(self, a, b):
        return not (b <= a*0.5 + 7 or b > a or (b > 100 and a < 100))

    def numFriendRequests(self, ages):
        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1

        prefix_age_sum = [0] * 121
        for i in range(121):
            prefix_age_sum[i] = age_count[i-1] + prefix_age_sum[i-1]

        res = 0
        for i in range(15, 121):
            if not age_count[i]:
                continue
            res += (prefix_age_sum[i] - prefix_age_sum[i // 2 + 7] - age_count[i // 2 + 7]) * age_count[i]
            res += age_count[i] * (age_count[i] - 1)
        return res