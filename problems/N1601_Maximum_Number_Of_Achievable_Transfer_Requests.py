class Solution(object):
    def maximumRequests_dfs(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        length = len(requests)
        status = [0]*n
        res = 0
        def dfs(index, status, current):
            nonlocal res
            if index >= length:
                if ''.join([str(i) for i in status]) == "0"*n:
                    res = max(res, current)
                    return
                return
            # include requests[index]
            status[requests[index][0]] -= 1
            status[requests[index][1]] += 1
            dfs(index+1, status, current+1)
            status[requests[index][0]] += 1
            status[requests[index][1]] -= 1

            # exclude requests[index]
            dfs(index + 1, status, current)

        dfs(0, status, 0)
        return res

    def maximumRequests(self, n, requests):
        length = len(requests)
        def check(state, n, requests):
            status = [0] * n
            for i in range(length):
                if (state >> i) & 1:
                    status[requests[i][0]] -= 1
                    status[requests[i][1]] += 1
            for i in range(n):
                if status[i]:
                    return False
            return True

        # Gospers-Hack : give several 0 and 1 , a fast way to get all permutation for them.
        for i in range(length, 0, -1):
            state = (1 << i) - 1
            while state < (1 << length):
                if check(state, n, requests):
                    return i
                c = state & -state
                r = state + c
                state = (((r^state) >> 2) // c) | r
        return 0


