"""
Use dictionary to save rain over lakes and an array to save dry-days
If we have two rain over for the same lakes, then check the dry-days to find one day to dry this lake.
Use binary search to find the day(first available day), if no such day , return no answer.
Here is a key point, need to make sure this day is as earlier as possible (test_avoidFlood_6)
"""
class Solution(object):
    def avoidFlood_bs(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import collections
        lakes = collections.defaultdict(list)
        dry_days = []
        days = len(rains)
        res = [0] * days
        for day in range(days):
            if rains[day] == 0:
                dry_days.append(day)
            else:
                lakes[rains[day]].append(day)
                if len(lakes[rains[day]]) > 1:
                    first = lakes[rains[day]][-2]
                    left,right = 0, len(dry_days)
                    previous = -1
                    while left < right:
                        mid = (right - left) // 2 + left
                        if dry_days[mid] > first:
                            previous = mid
                            right = mid
                        else:
                            left = mid+1
                    if previous > -1:
                        res[dry_days[previous]] = rains[day]
                        res[day] = -1
                        del lakes[rains[day]][-2]
                        del dry_days[previous]
                    else:
                        return []
                else:
                    res[day] = -1
        for i in range(days):
            if res[i] == 0:
                res[i] = 1
        return res

    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        import collections
        import bisect
        lakes = collections.defaultdict(list)
        dry_days = []
        days = len(rains)
        res = [0] * days
        for day in range(days):
            if rains[day] == 0:
                dry_days.append(day)
            else:
                lakes[rains[day]].append(day)
                if len(lakes[rains[day]]) > 1:
                    first = lakes[rains[day]][-2]
                    index = bisect.bisect_left(dry_days, first)
                    if index < len(dry_days):
                        res[dry_days[index]] = rains[day]
                        res[day] = -1
                        del lakes[rains[day]][-2]
                        del dry_days[index]
                    else:
                        return []
                else:
                    res[day] = -1
        for i in range(days):
            if res[i] == 0:
                res[i] = 1
        return res


