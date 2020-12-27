import collections
from collections import deque
"""
Usually, return the minimum steps/paths are BFS related. 

Here is a difficult point: 
[7,7,.....7,7,11]

"""

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        if length == 1:
            return 0
        mapping = collections.defaultdict(list)
        for i, n in enumerate(arr):
            mapping[n].append(i)

        res = 0
        visited = [0]*length
        visited[0] = 1
        queue = deque([0])

        while queue:
            l = len(queue)
            while l:
                idx = queue.popleft()
                if idx == length - 1:
                    return res
                visited[idx] = 1
                if idx + 1 < length and not visited[idx+1]:
                    queue.append(idx+1)
                if idx - 1 >= 0 and not visited[idx-1]:
                    queue.append(idx-1)
                for j in mapping[arr[idx]]:
                    if j == idx or visited[j]:
                        continue
                    queue.append(j)
                # This is the key point to avoid TLE
                del mapping[arr[idx]]
                l -= 1
            res += 1
        return res





