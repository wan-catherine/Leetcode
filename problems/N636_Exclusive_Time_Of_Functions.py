class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0]*n
        stack = []
        prev = 0
        for log in logs:
            vals = log.split(":")
            id, status, time = int(vals[0]), vals[1], int(vals[2])
            if status == 'start':
                if stack:
                    res[stack[-1][0]] += time - prev
                    prev = time
                stack.append((id, status, time))
            else:
                stack.pop()
                res[id] += time - prev + 1
                prev = time + 1 # this is the key part, make the end same as start.
        return res


