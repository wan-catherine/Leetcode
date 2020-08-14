class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        length = len(S)
        pos = -length
        left_distance = []
        for i in range(length):
            if S[i] == C:
                left_distance.append(0)
                pos = i
            else:
                left_distance.append(i - pos)

        pos = 2 * length
        for i in range(length - 1, -1, -1):
            if S[i] == C:
                pos = i
                continue
            else:
                left_distance[i] = min(left_distance[i], pos - i)
        return left_distance