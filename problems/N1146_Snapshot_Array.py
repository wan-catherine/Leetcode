import bisect


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        i = bisect.bisect(self.array[index], [snap_id + 1]) - 1
        return self.array[index][i][1]

# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0, 5)
print(obj.snap())
obj.set(0, 6)
print(obj.get(0,0))