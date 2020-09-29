class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length = len(S)
        count = 0
        for i in range(length):
            s = S[i]
            if s.isalpha():
                count += 1
                if count == K:
                    return s
            else:
                times = int(s) * count
                if times < K:
                    count = times
                else:
                    if K % count == 0:
                        return self.decodeAtIndex(S[:i], count)
                    else:
                        return self.decodeAtIndex(S[:i], K%count)

