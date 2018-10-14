class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == None and s2 == None:
            return True

        if sorted(s1) != sorted(s2):
            return False

        return self.helper(s1, s2)

    def helper(self, s1, s2):
        print(s1, s2)

        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        res = False

        for i in range(1,len(s1)):
            if (self.helper(s1[:i], s2[:i]) and self.helper(s1[i:], s2[i:]) or
                self.helper(s1[:i], s2[-i:]) and self.helper(s1[i:], s2[:-i])):
                res = True
                break

        return res
