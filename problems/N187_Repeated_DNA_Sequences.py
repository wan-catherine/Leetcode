import collections


class Solution(object):
    def findRepeatedDnaSequences_dict(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counter = collections.defaultdict(int)
        length = len(s)
        for i in range(length - 9):
            counter[s[i:i+10]] += 1
        return [key for key, value in counter.items() if value > 1]

    def findRepeatedDnaSequences_set(self, s):
        counter = set()
        res = set()
        length = len(s)
        for i in range(length - 9):
            temp = s[i:i+10]
            if temp in counter:
                res.add(temp)
            else:
                counter.add(temp)
        return list(res)

    """
    We only have 4 different chars here , and it can be represented as 0,1,2,3, so two bits. 
    Then 10-letter-long sequences can be represented as 20 bits . 
    So use bit manipulation. 
    
    Notice need to use mask + (1<<20)-1 to remove all possible '1' after 20th bits. 
    """
    def findRepeatedDnaSequences(self, s):
        length = len(s)
        if length <= 10:
            return []
        mapping = {'A':0, 'C':1, 'G':2, 'T':3}
        hash = 0
        for i in range(10):
            hash = (hash << 2) | mapping[s[i]]
        seen = set()
        mask = (1 << 20) - 1
        seen.add(hash)
        mulitple = set()
        res = []

        for i in range(10, length):
            hash = (hash << 2) & mask
            hash |= mapping[s[i]]
            if hash not in seen:
                seen.add(hash)
            else:
                if hash not in mulitple:
                    res.append(s[i-9:i+1])
                    mulitple.add(hash)
        return res