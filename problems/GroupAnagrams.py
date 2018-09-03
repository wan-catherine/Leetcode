class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            ss = sorted(s)
            key = ''.join(ss)
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        res = []
        for key in d:
            res.append(d[key])

        return res
