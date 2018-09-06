class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        count = {}
        for i in candidates:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        r = [[]] * (target + 1)
        if 1 in candidates:
            r[1] = [[1]]
        else:
            r[1] = []

        i = 2
        while i <= target:
            if i in candidates:
                r[i] = [[i]]
            else:
                r[i] = []

            k = 1
            while k <= i // 2:
                if r[i - k] != [] and r[k] != []:
                    for p in r[i - k]:
                        for q in r[k]:
                            l = p + q
                            l.sort()

                            if self.isNormal(l, count) and l not in r[i]:
                                r[i].append(l)
                k += 1
            i += 1

        return r[target]

    def isNormal(self, l, count):
        res = True
        number = {}
        for i in l:
            if i not in number:
                number[i] = 1
            else:
                number[i] += 1

        for i, j in number.items():
            if j > count[i]:
                res = False
                break
        return res
