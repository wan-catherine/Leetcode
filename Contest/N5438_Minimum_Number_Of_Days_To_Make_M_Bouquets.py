"""
Binary search

search from [min(day), max(day)]
if day x can get more than m bouquets, then serach the left part , otherwith ,search right part .

get_bouquets_for_day is similar as problem : 1437

Time complexity is O(nlgn)
"""
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if not bloomDay:
            return -1
        length = len(bloomDay)
        if m*k > length:
            return -1

        min_day = min(bloomDay)
        max_day = max(bloomDay) + 1
        while min_day < max_day:
            mid = (max_day - min_day) // 2 + min_day
            bouquet = self.get_bouquets_for_day(mid, bloomDay, k, length)
            if bouquet >= m:
                max_day = mid
            elif bouquet < m:
                min_day = mid + 1
        return min_day

    def get_bouquets_for_day(self, day, bloomDay, k, length):
        res = 0
        count = 0
        for i in range(length):
            if bloomDay[i] <= day:
                count += 1
                if count == k:
                    res += 1
                    count = 0
            else:
                count = 0
        return res