class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        length = len(s)
        arr = [ord(s[i]) - ord('a') + 1 for i in range(length)]
        base = 0
        for i in range(k):
            base += arr[i] * (power ** i)
        if base % modulo == hashValue:
            return s[:k]
        for i in range(k, length):
            base -= arr[i - k]
            base //= power
            base += arr[i] * (power ** (k - 1))
            if base % modulo == hashValue:
                return s[i - k + 1:i + 1]