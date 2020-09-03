class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if not b:
            return 0
        a_set, b_set = set(a), set(b)
        if b_set.difference(a_set):
            return -1

        new_b = b.replace(a, '')
        count = (len(b) - len(new_b))//len(a)
        if not new_b:
            return count
        if b in a*(count + 1):
            return count + 1
        if b in a*(count + 2):
            return count + 2

        return -1
