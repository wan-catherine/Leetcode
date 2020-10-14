class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        length = len(arr)
        visited = set()
        def dfs(index):
            if arr[index] == 0:
                return True
            if index in visited:
                return False
            visited.add(index)
            i = index + arr[index]
            if i >= 0 and i < length:
                if dfs(i):
                    return True
            j = index - arr[index]
            if j >= 0 and j < length:
                return dfs(j)

        return dfs(start)