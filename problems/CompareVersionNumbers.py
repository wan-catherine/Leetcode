class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        lv1 = len(v1)
        lv2 = len(v2)

        i = 0
        while i < lv1 and i < lv2:
            num1 = int(v1[i])
            num2 = int(v2[i])
            if num1 < num2:
                return -1
            if num1 > num2:
                return 1
            i += 1

        if lv1 > lv2:
            for j in range(i, lv1):
                if int(v1[j]) != 0:
                    return 1
            return 0
        else:
            for j in range(i, lv2):
                if int(v2[j]) != 0:
                    return -1
            return 0
