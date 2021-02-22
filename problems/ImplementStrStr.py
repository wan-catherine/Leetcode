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

    def strStr_KMP(self, haystack, needle):
        if needle == "":
            return 0
        pattern = self.findPattern(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] != needle[j]:
                if j != pattern[j]:
                    i -= 1
                j = pattern[j]
            else:
                j += 1
                if j == len(needle):
                    return i - j + 1
            i += 1
        return -1

    def findPattern(self, needle):
        pattern = [0] * len(needle)
        j = 0
        for i in range(2, len(needle)):
            while j != 0 and needle[i - 1] != needle[j]:
                j = pattern[j]
            if needle[i - 1] == needle[j]:
                j += 1
                pattern[i] = j
            else:
                pattern[i] = 0
        return pattern


