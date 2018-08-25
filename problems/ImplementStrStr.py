class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if haystack == "":
            return -1

        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
                i += 1
                if j == len(needle):
                    return i - j
            else:
                if j == 0:
                    i += 1
                else:
                    i = i - j + 1
                j = 0


        if j < len(needle):
            return -1
