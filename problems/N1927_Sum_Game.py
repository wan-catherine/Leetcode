"""
Think about two situations here :
1. l == r == 1, Bob wins if : ln == rn
2. l == 2 , r == 0 (or vice verse), Bob wins if : rn - ln == 9

then l, r, we need to combine #1 and #2 .

"""
class Solution:
    def sumGame(self, num: str) -> bool:
        length = len(num)
        l, ln, r, rn = 0, 0, 0, 0
        for i in range(length):
            if i < length//2:
                if num[i] == '?':
                    l += 1
                else:
                    ln += int(num[i])
            else:
                if num[i] == '?':
                    r += 1
                else:
                    rn += int(num[i])
        if (l + r) % 2 :
            return True
        return False if (ln - rn) == (r - l) * 9 // 2 else True


