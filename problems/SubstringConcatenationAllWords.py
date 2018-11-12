# SubstringConcatenationAllWords
import re
class Solution:
    def findSubstring_before(self, s, words):
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
                i = i - count + 1
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

    def findSubstring(self, s, words):
        if words == None or len(words) == 0 or len(words[0]) == 0:
            return []
        words = sorted(words)
        numWords = len(words)
        lenWords = len(words) * len(words[0])
        if s == None or len(s) < lenWords:
            return []

        i = 0
        temp = []
        res = []
        while i <= len(s) - lenWords:
            index = i
            temp = []
            for j in words:
                temp.append(s[index:index+len(words[0])])
                index += len(words[0])
            temp = sorted(temp)
            if temp == words:
                res.append(i)
            #     i += len(words[0])
            # else:
            i += 1

        return res