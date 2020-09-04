"""
BFS

"""
class Solution(object):
    def openLock_bfs(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        count = 0
        visited = [0]*10000
        target = int(target)
        if target == 0:
            return 0
        for t in deadends:
            visited[int(t)] = 1
        stack = [0]
        visited[0] = 1
        while stack:
            new_stack = []
            for num in stack:
                numbers = self.scroll(num)
                for n in numbers:
                    if visited[n]:
                        continue
                    if n == target:
                        return count + 1
                    visited[n] = 1
                    new_stack.append(n)
            count += 1
            stack = new_stack
        return -1

    def scroll(self, num):
        li = list(str(num).zfill(4))
        res = []
        for i in range(4):
            for d in [1, -1]:
                n = int(li[i])
                n = (n + d + 10) % 10
                temp = li[:]
                temp[i] = str(n)
                res.append(int(''.join(temp)))
        return res

    """
    Bi-directional BFS
    Notice : use set not list
    """
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if target in deadends or '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        mapping = {"0": ["9", "1"], "1": ["0", "2"], "2": ["1", "3"], "3": ["2", "4"], "4": ["3", "5"], "5": ["4", "6"], "6": ["5", "7"], "7": ["6", "8"], "8": ["7", "9"], "9": ["8", "0"]}
        visited_left, visited_right = set(), set()
        visited_left.add('0000')
        visited_right.add('target')

        stack_left, stack_right = ['0000'], [target]
        step_left, step_right = 0, 0
        while stack_left and stack_right:
            new_left = set()
            step_left += 1
            for node in stack_left:
                for i, c in enumerate(node):
                    for t in mapping[c]:
                        temp = node[:i] + t + node[i+1:]
                        if temp in stack_right:
                            return step_left + step_right
                        if temp not in deadends and temp not in visited_left:
                            new_left.add(temp)
                            visited_left.add(temp)
            stack_left = new_left

            new_right = set()
            step_right += 1
            for node in stack_right:
                for i, c in enumerate(node):
                    for t in mapping[c]:
                        temp = node[:i] + t + node[i+1:]
                        if temp in stack_left:
                            return step_left + step_right
                        if temp not in deadends and temp not in visited_right:
                            new_right.add(temp)
                            visited_right.add(temp)
            stack_right = new_right
        return -1