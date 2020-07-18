import collections


class Solution:
    def findOrder_old(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses < 1:
            return []

        count = [0]*numCourses
        dic = {}
        for l in prerequisites:
            count[l[0]] += 1
            if l[1] not in dic:
                dic[l[1]] = [l[0]]
            else:
                dic[l[1]].append(l[0])

        res = [i for i in range(len(count)) if count[i] == 0]
        if len(res) < 1:
            return []
        temp = res.copy()

        while len(res) < numCourses:
            if len(temp) < 1:
                break
            i = temp.pop()
            if i not in dic:
                continue
            for j in dic[i]:
                count[j] -= 1
                if count[j] == 0:
                    res.append(j)
                    temp.append(j)

        if len(res) == numCourses:
            return res
        else:
            return []

    def findOrder_dfs(self, numCourses, prerequisites):
        self.graph = {}
        for pair in prerequisites:
            self.graph.setdefault(pair[1], []).append(pair[0])
        self.status = [0] * numCourses
        self.result = []
        flag = True
        for i in range(numCourses):
            if i not in self.graph:
                self.result.append(i)
                continue
            flag = self.dfs(i)
            if not flag:
                break
        return self.result if flag else []

    """
    status has three value : 
        1 : visited ans success add into res
        0: not visited yet
        -1: during the visiting , but not add into res
    """
    def dfs(self, i):
        if self.status[i] == 1:
            return True
        if self.status[i] == -1:
            return False

        self.status[i] = -1
        for node in self.graph[i]:
            if node not in self.graph:
                continue
            if not self.dfs(node):
                return False

        self.status[i] = 1
        self.result = [i] + self.result   # add the new one in the head of self.result
        return True

    def findOrder_(self, numCourses, prerequisites):
        graph = {}
        indegree_count = [0] * numCourses
        for pair in prerequisites:
            graph.setdefault(pair[1], []).append(pair[0])
            indegree_count[pair[0]] += 1

        zero_indegree = [ i for i in range(numCourses) if not indegree_count[i]]
        res = []
        while zero_indegree:
            i = zero_indegree.pop()
            res.append(i)
            if i in graph:
                for node in graph[i]:
                    indegree_count[node] -= 1
                    if not indegree_count[node]:
                        zero_indegree.append(node)
        return [] if sum(indegree_count) else res


