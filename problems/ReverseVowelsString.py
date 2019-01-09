class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i = 0
        j = len(s) - 1
        res = list(s)
        while i <= j:
            if res[i] not in vowels and res[j] in vowels:
                i += 1
            elif res[i] in vowels and res[j] not in vowels:
                j -= 1
            elif res[i] not in vowels and res[j] not in vowels:
                i += 1
                j -= 1
            elif res[i] in vowels and res[j] in vowels:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return ''.join(res)
