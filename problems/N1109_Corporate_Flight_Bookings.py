class Solution(object):
    def corpFlightBookings_timeout(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        for info in bookings:
            start = info[0]
            end = info[1]
            num = info[2]
            for index in range(start, end+1):
                res[index] += num
        return res[1:]

    def corpFlightBookings(self, bookings, n):
        diff_array = [0] * (n+2)
        for info in bookings:
            diff_array[info[0]] += info[2]
            diff_array[info[1]+1] -= info[2]

        res = [0]*n
        cur = 0
        for i in range(n):
            cur += diff_array[i+1]
            res[i] = cur
        return res

