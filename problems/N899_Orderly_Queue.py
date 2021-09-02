class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        sset = set(s)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c in sset:
                break
        length = len(s)
        prev = s
        for i in range(length):
            if s[i] == c:
                ns = s[i:] + s[:i]
                if ns < prev:
                    prev = ns
        return prev

