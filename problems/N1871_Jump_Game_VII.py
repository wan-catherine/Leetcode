"""
Classical diff array!!!
"""
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False
        length = len(s)
        diff = [0] * (length + 1)
        diff[minJump] = 1
        diff[maxJump + 1] = -1
        reach = 0
        for i in range(1, length):
            reach += diff[i]
            if not reach:
                continue
            if s[i] == '1':
                continue
            if i + minJump <= length:
                diff[i + minJump] += 1
            if i + maxJump + 1 <= length:
                diff[i + maxJump + 1] += -1
        return reach != 0