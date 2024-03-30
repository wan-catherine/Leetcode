class Solution:
    def minSwaps_(self, s: str) -> int:
        cur, res = 0, 0
        for c in s:
            if c == '[':
                cur += 1
            else:
                cur -= 1
                if cur < 0:
                    res += 1
                    cur += 2
        return res

    """
    ]][[ only need one swap by sway the first and the last 
    ][ need one swap 
    
    so the unmatched number // 4 +  (1 if has 2 left or 0)
    """
    def minSwaps(self, s: str) -> int:
        length = len(s)
        stack = []
        for i in range(length):
            if stack and stack[-1] == '[' and s[i] == ']':
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            return 0

        l = len(stack)
        if l == 2:
            return 1
        else:
            return l // 4 + (1 if l % 4 == 2 else 0)