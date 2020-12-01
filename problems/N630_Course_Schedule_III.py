import heapq
"""
Greedy:
    1. Sort by deadline, we need to deal with earlier deadline.
    2. If current + t <= d, then we can take this course.
    3. If not, then we can check the t with the longest tt in the courses we take before. 
        a. if longest t <= tt, then do nothing. 
        b. if longest t > tt, then we use this course and remove the longest course. This way we can save some time. 
        because t > tt, and we sort by deadline, so we can definitely change t to tt . 
        KEY POINT: t > tt, d < dd ==> use tt instead. 
"""

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x:x[1])
        res, current = 0, 0
        heap = []
        for t, d in courses:
            if current + t <= d:
                heapq.heappush(heap, (-t, d))
                res += 1
                current += t
            else:
                if heap and abs(heap[0][0]) > t:
                    tt, dd = heapq.heappop(heap)
                    current += tt
                    current += t
                    heapq.heappush(heap, (-t, d))
        return res

