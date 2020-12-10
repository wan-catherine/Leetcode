import sys
"""
TSP : travelling salesman problem
Totally there is length different node. 
We use bit mask as all status of those nodes :
    dp[mask][last] : minimum length by using the several nodes (mask bit is 1 which means this node be used) , and the last node is last. 
    
    dp[mask][last] = min(dp[mask - (1<<j)][j] + distances[(j, last)]) j != last and j in mask's 1 bit. 
    
We also need a parent to mark all the last nodes, so we can get the real sequence. 
"""

class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        length = len(A)

        def get_dist():
            distances = {}
            for i in range(length):
                for j in range(length):
                    for index in range(len(A[i])):
                        if A[j].startswith(A[i][index:]):
                            distances[(i, j)] = len(A[j]) - (len(A[i]) - index)
                            break
                    else:
                        distances[(i, j)] = len(A[j])
            return distances

        distances = get_dist()
        dp = [[sys.maxsize] * length for _ in range(1<<length)]
        parent = [[-1]*length for _ in range(1<<length)]
        for i in range(length):
            dp[1<<i][i] = len(A[i])

        for state in range(1, 1<<length):
            for last in range(length):
                if state & (1 << last) != (1 << last):
                    continue
                if state - (1 << last) == 0:
                    continue
                for prev in range(length):
                    if prev == last or (state & (1 << prev) != (1 << prev)):
                        continue
                    val = dp[state - (1 << last)][prev] + distances[(prev, last)]
                    if val < dp[state][last]:
                        dp[state][last] = val
                        parent[state][last] = prev
        minimum = sys.maxsize
        end = -1
        for i in range(length):
            if dp[-1][i] < minimum:
                minimum = dp[-1][i]
                end = i

        res = []
        state = (1 << length) - 1
        for _ in range(length):
            res.append(end)
            old_end = end
            end = parent[state][end]
            state -= (1 << old_end)

        res.reverse()
        ans = A[res[0]]
        for i in range(1, len(res)):
            d = distances[(res[i-1], res[i])]
            ans += A[res[i]][-d:]
        return ans





