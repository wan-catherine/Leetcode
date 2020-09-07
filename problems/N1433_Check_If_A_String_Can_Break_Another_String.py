class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        one = sorted(list(s1))
        two = sorted(list(s2))
        length = len(s1)

        for i in range(length):
            if one[i] == two[i]:
                continue
            flag = True if one[i] > two[i] else False
            break

        for i in range(1, length):
            if one[i] == two[i]:
                continue
            if (one[i] > two[i]) != flag:
                return False
        return True
