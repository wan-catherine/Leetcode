import collections
"""
Use dictionary to save the status.

"""

class Solution(object):
    def get_pure_name_int(self,name):
        if '(' in name and ')' in name:
            start_index = name.rindex('(')
            end_index = name.rindex(')')
            pure_n = name[:start_index]
            value = int(name[start_index + 1: end_index])
        else:
            pure_n = name
            value = 0
        return (pure_n, value)

    def getFolderNames_timeout(self, names):
        if not names:
            return []

        res = []
        cache = collections.defaultdict(list)
        for name in names:
            pure_n, value = self.get_pure_name_int(name)
            if name not in cache:
                cache[name].append(0)
                res.append(name)
                if pure_n != name and value > 0:
                    cache[pure_n].append(value)
                continue
            tails = cache[name]
            if 0 not in tails:
                res.append(name)
                cache[pure_n].append(value)
                cache[name].append(0)
                continue
            j = 1
            while j in tails:
                j += 1
            new_name = name + "(" + str(j) + ")"
            cache[new_name].append(0)
            res.append(new_name)
            cache[name].append(j)
        # print(res)
        return res

    def getFolderNames(self, names):
        if not names:
            return []
        res = []
        cache = collections.defaultdict(int)
        for name in names:
            if name not in cache:
                res.append(name)
                cache[name] = 1
                continue
            j = cache[name]
            while True:
                new_name = f"{name}({j})"
                if new_name not in cache:
                    cache[new_name] = 1
                    cache[name] = j+1
                    res.append(new_name)
                    break
                j += 1
        return res





