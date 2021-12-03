from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.cols, self.rows = height, width
        self.grid = [[0] * width for _ in range(height)]
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dirs = ['East', 'North', 'West', 'South']
        self.pos = [0, 0]
        self.dir = 0
        self.total = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        num = num % self.total
        r, c = self.pos
        # I don't understand why need to update this !!!
        if num == r == c == 0:
            self.dir = 3
        while num:
            row, col = r + self.directions[self.dir][0], c + self.directions[self.dir][1]
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                self.dir += 1
                self.dir %= 4
                continue
            r, c = row, col
            num -= 1
        self.pos = [r, c]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dirs[self.dir]

# Your Robot object will be instantiated and called as such:
obj = Robot(97,98)
obj.step(2)
obj.step(2)
print(obj.getPos())
print(obj.getDir())
obj.step(2)
obj.step(1)
obj.step(4)
print(obj.getPos())
print(obj.getDir())
