"""
Reverse sort the position.
If some cars can pass the head one, then ignore it .
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if not position:
            return 0

        length = len(position)
        mapping = {}
        for i, p in enumerate(position):
            mapping[p] = speed[i]
        position.sort(reverse=True)

        res, i = 1, 1
        current_p, current_s = position[0], mapping[position[0]]
        while i < length:
            next_p, next_s = position[i], mapping[position[i]]
            if current_s >= next_s:
                res += 1
                current_p, current_s = next_p, next_s
                i += 1
                continue
            current_t, next_t = (target - current_p) / current_s, (target - next_p) / next_s
            if current_t < next_t:
                res += 1
                current_p, current_s = next_p, next_s
                i += 1
                continue
            i += 1
        return res


