import collections


class Solution:
    # topological sort
    def canFinish_old(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites == None or len(prerequisites) == 0:
            return True

        courseMap = {}
        level = [0] * numCourses
        for pair in prerequisites:
            courseMap.setdefault(pair[1],[]).append(pair[0])
            level[pair[0]] += 1

        courses = [i for i in range(len(level)) if level[i] == 0]
        while len(courses) > 0:
            course = courses.pop()
            if course in courseMap:
                for i in courseMap[course]:
                    if level[i] > 0:
                        level[i] -= 1
                        if level[i] == 0:
                            courses.append(i)
        return False if sum(level) else True

    # DFS
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites:
            return True

        self.graph = {}
        for pair in prerequisites:
            self.graph.setdefault(pair[0], []).append(pair[1])

        self.status = [0] * numCourses
        for i in range(numCourses):
            if i not in self.graph:
                continue
            if not self.dfs(i):
                return False
        return True

    def dfs(self,i):
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
        return True

    """
    calculate all indegree. 
    """
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        for c, c_p in prerequisites:
            graph[c_p].add(c)
            indegree[c] += 1
        visited = [0]*numCourses
        stack = [i for i in range(numCourses) if i not in indegree]
        count = 0
        while stack:
            course = stack.pop()
            visited[course] = 1
            for c in graph[course]:
                if visited[c]:
                    continue
                indegree[c] -= 1
                if not indegree[c]:
                    stack.append(c)
            count += 1
        return count == numCourses
