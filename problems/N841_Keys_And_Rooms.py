class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        length = len(rooms)
        status = [0]*length
        def dfs(n):
            if status[n]:
                return
            status[n] = 1
            for key in rooms[n]:
                dfs(key)

        dfs(0)
        return 0 not in status