class Solution:
    def canFinish(self, numCourses, prerequisites):
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
            if pair[1] not in courseMap:
                courseMap[pair[1]] = [pair[0]]
            else:
                courseMap[pair[1]].append(pair[0])
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

        for i in level:
            if i != 0:
                return False
        return True


