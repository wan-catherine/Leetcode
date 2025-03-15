class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        length = len(s)
        right = [0] * length
        for i in range(length - 2, -1, -1):
            if s[i+1] == '1':
                right[i] = right[i+1] + 1
        res = 0
        for i in range(length):
            if s[i] == '1':
                res += right[i] + 1
        for zero in range(1, 201):
            j = 0
            cur = 0
            dz = zero ** 2
            for i in range(length - zero):
                while j < length and cur < zero:
                    if s[j] == '0':
                        cur += 1
                    j += 1
                if cur < zero:
                    break
                one = j - i - zero
                if right[j-1] + one >= dz:
                    extra = right[j-1] - max(0, dz - one)
                    res += max(0, extra + 1)
                if s[i] == '0':
                    cur -= 1
        return res

