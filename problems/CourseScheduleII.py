class Solution:
    def findOrder(self, numCourses, prerequisites):
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




