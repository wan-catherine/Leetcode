import bisect


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        length = len(people)
        start, end = 0 , length - 1
        res = 0
        while start <= end:
            if start == end:
                res += 1
                break
            value = people[start] + people[end]
            if value <= limit:
                res += 1
                start += 1
                end -= 1
            else :
                res += 1
                end -= 1
        return res

