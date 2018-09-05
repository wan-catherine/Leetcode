class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
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
                            if l not in r[i]:
                                r[i].append(l)
                k += 1
            i += 1

        return r[target]

