import collections


class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        words_map = collections.defaultdict(list)
        letters_map = collections.defaultdict(list)
        for word in wordlist:
            words_map[word.lower()].append(word)
            letters_map[frozenset(word.lower() + 'aeiou' )].append(word.lower())

        res = []
        for word in queries:
            word_lower = word.lower()
            if word_lower in words_map:
                if word in words_map[word_lower]:
                    res.append(word)
                else:
                    res.append(words_map[word_lower][0])
            else:
                letter = frozenset(word_lower + 'aeiou')
                if letter not in letters_map:
                    res.append("")
                    continue
                for key in letters_map[letter]:
                    if len(key) != len(word):
                        continue
                    length = len(word)
                    for i in range(length):
                        if word_lower[i] != key[i] and (word_lower[i] not in ['a', 'e', 'i', 'o', 'u'] or key[i] not in ['a', 'e', 'i', 'o', 'u']):
                            break
                    else:
                        res.append(words_map[key][0])
                        break
                else:
                    res.append("")
        return res

