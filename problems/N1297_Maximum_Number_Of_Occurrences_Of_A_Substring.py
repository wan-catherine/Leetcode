import collections
"""
I first used fix sliding windows. Then we have [minSize, maxSize+1] different slding windows. 

But here is the key point : 
If a string have occurrences x times,
any of its substring must appear at least x times.

So actually we can use the minSize as the length of sliding widnows.
"""

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        mapping = collections.defaultdict(int)
        length = len(s)
        if length < minSize:
            return 0
        # fix the sliding widows' length
        start, end = 0, 0
        count = collections.defaultdict(int)
        while end < length:
            if end - start + 1 < minSize:
                count[s[end]] += 1
                end += 1
            else:
                count[s[end]] += 1
                c_len = len(count.keys())
                if c_len <= maxLetters:
                    mapping[s[start:end+1]] += 1

                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1
                end += 1
        mapping[0] = 0
        print(mapping)
        return max(mapping.values())

    def maxFreq_others(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        numOfOccurences = {}

        for i in range(len(s) - minSize + 1):
            currentString = s[i:i + minSize]

            if currentString in numOfOccurences:
                numOfOccurences[currentString] += 1
            else:
                if len(set(currentString)) <= maxLetters:
                    numOfOccurences[currentString] = 1
        print(numOfOccurences)
        if not numOfOccurences:
            return 0
        return max(numOfOccurences.values())


