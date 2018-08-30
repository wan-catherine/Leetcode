# SubstringConcatenationAllWords
import re
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # [m.start() for m in re.finditer('test', 'test test test test')]
        indexs = []
        for word in set(words):
            l = [m.start() for m in re.finditer(word,s)]
            indexs.extend(l)

        indexs.sort()
        if len(words) <= 1:
            return indexs

        wordCount = {word:0 for word in words }
        wordRes = {word:0 for word in words }
        for w in words:
            wordRes[w] += 1

        lenght = len(words[0])
        count = 1

        res = []
        wordCount[s[indexs[0]:indexs[0] + lenght]] = 1
        i = 1
        while i < len(indexs):
            if indexs[i] - indexs[i - 1] != lenght and count > 0:
                self.clearDice(wordCount)
                count = 0
                i += 1
                continue
            currentWord  = s[indexs[i]:indexs[i] + lenght]
            if wordCount[currentWord] > wordRes[currentWord] - 1:
                self.clearDice(wordCount)
                wordCount[currentWord] = 1
                count = 1
                
            else:
                wordCount[currentWord] += 1
                count += 1

            if count == len(words):
                k = indexs[i - len(words) + 1]
                res.append(k)
                self.clearDice(wordCount)
                count = 0
                if i > i - len(words) + 2:
                    i = i - len(words) + 2
                    continue
            i += 1
        return res

    def clearDice(self, wordCount):
        for i in wordCount:
            wordCount[i] = 0
