class Solution(object):
    def processQueries_my_solution(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        permutation = [i for i in range(1,m+1)]
        res = []
        for num in queries:
            for i in range(m):
                if permutation[i] == num:
                    res.append(i)
                    permutation = [num] + permutation[:i] + (permutation[i+1:] if i + 1 < m else [])
                    break
        return res

    def processQueries(self, queries, m):
        permutation = [i for i in range(1, m + 1)]
        res = []
        for num in queries:
            index = permutation.index(num)
            res.append(index)
            del permutation[index]
            permutation.insert(0, num)
        return res