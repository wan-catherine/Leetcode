import collections


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        length = len(word)
        vowels = "aeiou"
        array = [0] * length
        cnt = 0
        for i in range(length - 1, -1, -1):
            if word[i] in vowels:
                cnt += 1
            else:
                cnt = 0
            array[i] = cnt

        cv, cc = 0, 0
        status = collections.defaultdict(int)
        res = 0
        j = 0
        for i in range(length):
            while j < length and (cv < 5 or cc < k):
                if word[j] in vowels:
                    status[word[j]] += 1
                    if status[word[j]] == 1:
                        cv += 1
                else:
                    cc += 1
                j += 1
            if cv == 5 and cc == k:
                res += (1 + (array[j] if j < length else 0))

            if word[i] in vowels:
                status[word[i]] -= 1
                if status[word[i]] == 0:
                    cv -= 1
            else:
                cc -= 1
        return res
