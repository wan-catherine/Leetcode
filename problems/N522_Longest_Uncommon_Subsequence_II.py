import collections

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        if not strs:
            return  -1
        str_set = set(strs)
        if len(str_set) == 1:
            return -1

        count = collections.Counter(strs)
        strs = sorted(str_set, key=lambda s:len(s), reverse=True)
        length = len(strs)
        res = -1
        for i in range(length):
            if count[strs[i]] > 1:
                continue
            if i == 0:
                return len(strs[i])
            flag = True
            for j in range(i):
                if self.check(strs[j], strs[i]):
                    flag = False
                    break
            if flag:
                res = len(strs[i])
                break
        return res

    def check(self, long, short):
        l_s, s_s = 0, 0
        l_len, s_len = len(long), len(short)
        while l_s < l_len and s_s < s_len:
            if long[l_s] == short[s_s]:
                l_s += 1
                s_s += 1
            else:
                l_s += 1

        if s_s == s_len:
            return True
        else:
            return False


