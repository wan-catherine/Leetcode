def rand7(self):
    pass

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        index = 50
        while index >= 40:
            index = 7 * (rand7() - 1) + (rand7() - 1);
        return index % 10 + 1