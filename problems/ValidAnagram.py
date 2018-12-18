class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t :
            return True
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()
        if ''.join(sl) != ''.join(tl):
            return False
        else:
            return True

    def isAnagram_nice_version(self, s, t):
        if len(s) != len(t):
            return False

        letters = 'abcdefghijklmnopqrstuvwxyz'
        for letter in letters:
            if s.count(letter) != t.count(letter):
                return False
        return True