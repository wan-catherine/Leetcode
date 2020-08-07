import collections
"""
Can't use DFS, because a friend of a friend can also be a friend.
"""

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        f = self.bfs(friends, id, level)
        res = collections.defaultdict(int)
        for i in f:
            if i == id:
                continue
            for w in watchedVideos[i]:
                res[w] += 1

        return sorted(res.keys(), key=lambda key:(res[key],key))

    def bfs(self, friends, id, level):
        queue = [id]
        count = 0
        seen = set(queue)
        while queue and count < level:  # bfs
            count += 1
            temp = set()
            for i in queue:
                for j in friends[i]:
                    if j not in seen:
                        temp.add(j)
                        seen.add(j)
            queue = temp
        return queue