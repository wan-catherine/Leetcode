"""
1 <= left.length, right.length <= 18
super-palindrome : 18  ==> palidrome : 9 ==> number : 5
10**18 ==> 10**9 ==> 10**5
    math.sqrt   construct palidrome
"""
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        l, r = int(left), int(right)
        res = 0
        # need to remember this
        def construct_pali(val, type):
            v = val
            # type == 1 means format like : aba
            # type == 0 means format like : aa
            if type == 1:
                val //= 10
            while val:
                v *= 10
                v += val % 10
                val //= 10
            return v

        for i in range(1, 10**5+1):
            for j in range(2):
                pali = construct_pali(i, j)
                if pali > 10**9:
                    continue
                super_pali = pali * pali
                if super_pali >= l and super_pali <= r and str(super_pali) == str(super_pali)[::-1]:
                    res += 1
        return res