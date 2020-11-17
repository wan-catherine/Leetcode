"""
Classical BFS (get the minimum steps to get somewhere).
The key point is how to set boundary.
If we keep moving forward, there is no endless. so at somepoint we need to backward.
Here we set limit.
when we get some point which is larger than > x+b, we can move backward.

"""
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        limit = 4001
        #limit = max(x, max(forbidden)) + b + 1 , we need to add 1, here

        res = 0
        stack = [(0,0)]
        visited = set()
        for i in forbidden:
            visited.add((i, 0))
            visited.add((i, 1))
        visited.add((0,0))
        while stack:
            new_stack = []
            res += 1
            for cur, direction in stack:
                # if we don't add 1 to limit, here we need to use cur <= limit
                if cur < limit and (cur + a,0) not in visited:
                    new_stack.append((cur + a, 0))
                    visited.add((cur+a,0))
                    if cur+a == x:
                        return res
                if not direction:
                    if cur - b >= 0 and (cur - b,1) not in visited:
                        new_stack.append((cur-b, 1))
                        visited.add((cur-b,1))
                        if cur-b == x:
                            return res
            stack = new_stack
        return -1
