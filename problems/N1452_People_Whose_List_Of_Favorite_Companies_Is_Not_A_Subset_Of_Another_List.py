class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        f_set = [set(companies) for companies in favoriteCompanies]
        length = len(favoriteCompanies)
        res = []
        for i in range(length):
            flag = False
            for j in range(length):
                if i == j:
                    continue
                if f_set[i].issubset(f_set[j]):
                    flag = True
                    break
            if not flag:
                res.append(i)
        return res