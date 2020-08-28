class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        prefix = shifts[:]
        length = len(shifts)
        for i in range(length-2, -1, -1):
            prefix[i] += prefix[i+1]
            prefix[i+1] %= 26

        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i in range(length):
            index = prefix[i]
            if index == 0:
                res.append(S[i])
            else:
                prev_index = alphabets.index(S[i])
                new_index = (prev_index + index) % 26
                res.append(alphabets[new_index])
        return ''.join(res)





