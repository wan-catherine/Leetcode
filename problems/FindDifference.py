class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sd = dict()
        for i in t:
            if i in sd:
                sd[i] += 1
            else:
                sd[i] = 1


        for i in s:
            if i in sd:
                sd[i] -= 1
            else:
                return i

        for key, value in sd.items():
            if value!=0:
                return key

