class Solution:
    def minimumBuckets_my(self, street: str) -> int:
        if '.' not in street:
            return -1

        length = len(street)
        if length >= 2:
            if street[:2] == 'HH' or street[-2:] == 'HH':
                return -1
        i = 0
        while i < length:
            if street[i] == '.':
                i += 1
                continue
            j = i
            while j < length and street[j] == 'H':
                j += 1
            if j - i > 2:
                return -1
            i = j
        street = list(street)
        res = 0
        i = 0
        while i < length - 2:
            if street[i] == 'H' and street[i + 1] == '.' and street[i + 2] == 'H':
                res += 1
                street[i] = street[i + 2] = '.'
                i += 3
            else:
                i += 1
        i = 0
        while i < length:
            if street[i] == '.':
                i += 1
                continue
            j = i
            while j < length and street[j] == 'H':
                j += 1
            if j - i > 2:
                return -1
            if j - i == 2 and i == 0:
                return -1
            res += j - i
            i = j
        return res

    """
    Greedy problem
    1. we only can check all 'H' position 
    2. check the left side has a bucket or not, if it has , nothing need to do
    3. check the right side , if it's '.', then put bucket there (so we can get as many as houses covered if we first check the right side)
    4. if not, then check the left side, if it's a '.', then put bucket
    5. if all doesn't work, then return -1
    """
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        length = len(street)
        res = 0
        for i in range(length):
            if street[i] != 'H':
                continue
            if i > 0 and street[i - 1] == '#':
                continue
            if i + 1 < length and street[i + 1] == '.':
                res += 1
                street[i + 1] = '#'
            elif i > 0 and street[i - 1] == '.':
                res += 1
                street[i - 1] = '#'
            elif i > 0 and street[i - 1] == '#':
                continue
            else:
                return -1
        return res