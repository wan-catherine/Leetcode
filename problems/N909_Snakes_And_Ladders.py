class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        index_num_mapping = {}
        num_index_mapping = {}
        reverse = not (n % 2)
        num = n*n
        for i in range(n):
            if reverse:
                for j in range(n):
                    index_num_mapping[(i, j)] = num
                    num_index_mapping[num] = (i, j)
                    num -= 1
            else:
                for j in range(n-1, -1, -1):
                    index_num_mapping[(i, j)] = num
                    num_index_mapping[num] = (i, j)
                    num -= 1
            reverse = not reverse
        x, y = num_index_mapping[n*n]
        stack = [(n-1,0)]
        moves = 0
        visited = set()
        while stack:
            new_stack = []
            for r, c in stack:
                if r == x and c == y:
                    return moves
                s = index_num_mapping[(r, c)]
                if s in visited:
                    continue
                visited.add(s)
                for i in range(1, 7):
                    if s+i > n*n:
                        break
                    row, col = num_index_mapping[s+i]
                    if board[row][col] != -1:
                        row, col = num_index_mapping[board[row][col]]
                    new_stack.append((row, col))
            stack = new_stack
            print(new_stack)
            moves += 1
        return -1

