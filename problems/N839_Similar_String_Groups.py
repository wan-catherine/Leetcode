class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        arr = list(set(strs))
        length = len(arr)
        parents = [i for i in range(length)]
        sizes = [1] * length

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(p, q):
            pp, pq = find(p), find(q)
            if pp == pq:
                return
            if sizes[pp] < sizes[pq]:
                parents[pp] = pq
                sizes[pq] += sizes[pp]
            else:
                parents[pq] = pp
                sizes[pp] += sizes[pq]

        def is_similar(a, b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                if count > 2:
                    return False
            return True

        for i in range(length):
            for j in range(i+1, length):
                if is_similar(arr[i], arr[j]):
                    union(i, j)

        for i in range(length):
            parents[i] = find(i)

        return len(set(parents))
