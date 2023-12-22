import collections


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        length = len(word)
        words = []
        prev = 0
        for i in range(1, length):
            if abs(ord(word[i]) - ord(word[i-1])) > 2:
                words.append(word[prev: i])
                prev = i
        if prev != length:
            words.append(word[prev:length])
        res = 0
        for st in words:
            l = len(st)
            for c in range(1, 27):
                if c * k > l:
                    break
                ct = collections.Counter(st[:c*k-1])
                for i in range(c*k-1, l):
                    ct[st[i]] += 1
                    flag = True
                    for v in ct.values():
                        if v != k:
                            flag = False
                            break
                    if flag:
                        res += 1
                    ct[st[i-c*k+1]] -= 1
                    if ct[st[i-c*k+1]] == 0:
                        del ct[st[i-c*k+1]]
        return res
