class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        n_frequency = {}
        for i in s:
            n_frequency[i] = n_frequency.setdefault(i,0) + 1

        f_n = {}
        for key, value in n_frequency.items():
            n_list = f_n.setdefault(value, [])
            n_list.append(key)

        res = ''
        for key in sorted(f_n.keys(), reverse=True):
            for c in f_n[key]:
                res += c * key

        return res
