"""
Also can use hashtable(dictionary) + binary search

use the binary search to findn the position of the letter .
In care we meet the same letter , so need to find the right-est position.
"""
import bisect
from collections import defaultdict


class Solution(object):
    def numMatchingSubseq_before(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        aph = [[] for _ in range(26)]
        s_len = len(S)
        for i in range(s_len):
            aph[ord(S[i]) - ord('a')].append(i)

        count = 0
        positive = set()
        for word in words:
            if word in positive:
                count += 1
                continue
            stack = []
            aph_index = [0] * 26
            flag = True
            for i in word:
                index = ord(i) - ord('a')
                while stack and aph_index[index] < len(aph[index]) and stack[-1] > aph[index][aph_index[index]]:
                    aph_index[index] += 1
                if aph_index[index] < len(aph[index]):
                    stack.append(aph[index][aph_index[index]])
                    aph_index[index] += 1
                else:
                    flag = False
                    break
            if flag:
                positive.add(word)
                count += 1
        return count

    def numMatchingSubseq(self, S, words):
        aph_dict = defaultdict(list)
        for i in range(len(S)):
            aph_dict[S[i]].append(i)
        count = 0
        for word in words:
            previous = -1
            flag = True
            for i in word:
                index = bisect.bisect(aph_dict[i], previous)
                if index == len(aph_dict[i]):
                    flag = False
                    break
                previous = aph_dict[i][index]
            if flag:
                count += 1
        return count





