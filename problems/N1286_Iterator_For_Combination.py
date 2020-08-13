class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.count = 0
        self.res = []
        self.dfs(characters, combinationLength, [])
        self.most_count = len(self.res)

    def dfs(self, characters, k, temp):
        if k == 0:
            self.res.append(temp[:])
        for i in range(len(characters)):
            temp.append(characters[i])
            self.dfs(characters[i+1:], k-1, temp)
            temp.pop()

    def next(self) -> str:
        if self.hasNext():
            res = ''.join(self.res[self.count])
            self.count += 1
            return res

    def hasNext(self) -> bool:
        if self.count < self.most_count:
            return True
        else:
            return False

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())