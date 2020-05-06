"""
Here is how to define status transform formula :
for string words1, and words2:
d[i][j] = min edit path for transforming from words1[0:i+1] to words2[0:j+1]
d[len(words1)][len(words2)] is the result

now we have three operations here : replace, delete, insert
so d[i][j] = min{d[i-1][j] + 1, d[i-1][j-1] + 1, d[i][j-1] + 1}
d[i-1][j]  --> d[i][j] : if words1[:i] is same as words2[:j+1], so we delete the ith in words1
d[i-1][j-1] --> d[i][j] : if words1[:i] is same as words2[:j], then we replace the words1[i] with words2[j]
d[i][j-1] --> d[i][j] : if words1[:i+1] is same as words2[:j], then we insert words2[j] into words1

how do we know the change path for the minimun edit path ?

"""

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1

        res = [[0]*(l2+1) for i in range(l1+1)]

        for i in range(l1+1):
            res[i][0] = i
        for j in range(l2+1):
            res[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i-1] == word2[j-1]:
                    res[i][j] = res[i-1][j-1]
                else:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
        return res[-1][-1]

    def minDistance_other(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        # generate the empty table
        table = [[0 for i in range(l2)] for j in range(l1)]

        # fill in the base case
        for i in range(l1):
            table[i][0] = i
        for j in range(l2):
            table[0][j] = j

        # fill in the table row by row
        for i in range(1, l1):
            for j in range(1, l2):

                # if two letters equal, pick diagonal
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]

                # if two letters differ, pick the min among upper,left and diagonal
                else:
                    table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1

        # return the bottom right cell
        return table[-1][-1]
