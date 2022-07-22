class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        bl = len(blacklist)
        arr = [n - bl + i for i in range(bl)]
        i = -1
        bs = set(blacklist)
        self.mapping = {}
        for b in blacklist:
            if b >= n - bl:
                continue
            while arr[i] in bs:
                i -= 1
            self.mapping[b] = arr[i]
            i -= 1
        self.r = n - bl

    def pick(self) -> int:
        val = random.randrange(0, self.r)
        if val in self.mapping:
            return self.mapping[val]
        return val 