class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        length = len(palindrome)
        if length == 1:
            return ''
        if length == 2:
            if palindrome[0] != 'a':
                return 'a' + palindrome[1]
            else:
                return 'ab'
        if length == 3:
            if palindrome[0] == 'a':
                return 'a' + palindrome[1] + 'b'
            else:
                return 'a' + palindrome[1:]

        if palindrome[0] != 'a':
            return 'a' + palindrome[1:]
        else:
            if palindrome[1] != 'a':
                return 'aa' + palindrome[2:]
            else:
                return palindrome[:-1] + 'b'