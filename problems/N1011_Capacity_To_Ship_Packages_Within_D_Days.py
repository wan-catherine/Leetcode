class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        max_weight = sum(weights) + 1
        min_weight = 1

        while min_weight < max_weight:
            mid = (max_weight - min_weight) // 2 + min_weight
            can_finish = self.can_finish_in_D_days(mid, weights, D)
            if can_finish:
                max_weight = mid
            else:
                min_weight = mid + 1
        return min_weight

    def can_finish_in_D_days(self, load, weights, D):
        days = 0
        temp = 0
        for w in weights:
            if w > load:
                return False
            if temp + w <= load:
                temp += w
            else:
                days += 1
                temp = w
        if temp > 0:
            days += 1
        if days > D:
            return False
        else:
            return True