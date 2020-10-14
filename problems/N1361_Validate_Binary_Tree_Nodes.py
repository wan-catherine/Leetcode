"""
A graph is a validate tree:
    1. there is only one node doesn't have parent
    2. except root node, all other nodes have only one parent
    3. there is no cycle in the graph
"""
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        parents = [-1]*n
        for i in range(n):
            if leftChild[i] != -1:
                if parents[leftChild[i]] != -1:
                    return False
                parents[leftChild[i]] = i
            if rightChild[i] != -1:
                if parents[rightChild[i]] != -1:
                    return False
                parents[rightChild[i]] = i
        res = 0
        key = 0
        for index, i in enumerate(parents):
            if i == -1:
                res += 1
                key = index
        if res != 1:
            return False
        visited = [0]*n

        def dfs(i):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            flag = True
            if leftChild[i] != -1:
                flag = flag and dfs(leftChild[i])
            if rightChild[i] != -1:
                flag = flag and dfs(rightChild[i])
            if not flag:
                return False
            visited[i] = 2
            return True

        res = dfs(key)
        return res and 0 not in visited
