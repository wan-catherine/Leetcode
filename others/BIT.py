class BIT:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def update(self, i, delta):
        idx = i
        while idx <= self.n:
            self.arr[idx] += delta
            idx += idx & (-idx)

    def query(self, idx):
        res = 0
        while idx:
            res += self.arr[idx]
            idx -= idx & (-idx)
        return res

    def range(self, left, right):
        if left > right:
            return 0
        return self.query(right) - self.query(left-1)
