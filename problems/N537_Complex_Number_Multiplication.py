class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        left = self.get_number(a)
        right = self.get_number(b)
        real = left[0]*right[0] - left[1]*right[1]
        complex = left[1]*right[0] + left[0]*right[1]
        return f"{real}+{complex}i"

    def get_number(self, s):
        index = s.index('+')
        a = int(s[:index])
        b = int(s[index + 1:-1])
        return (a,b)