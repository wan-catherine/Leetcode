class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == " " or len(s) < 1:
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            if i == len(s):
                return True
            while not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True