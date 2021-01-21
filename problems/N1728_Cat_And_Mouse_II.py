from collections import deque

class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        status = {}
        step = 0
        queue = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                elif grid[i][j] == 'F':
                    food = (i, j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '#':
                    continue
                for t in range(1, 3):
                    queue.append((i, j, i, j, t))
                    status[(i, j, i, j, t)] = 2
                    if (i, j) == food:
                        continue
                    queue.append((i, j, food[0], food[1], t))
                    status[(i, j, food[0], food[1],t)] = 2
                    queue.append((food[0], food[1], i, j, t))
                    status[(food[0], food[1], i, j, t)] = 1
   
        def find_prev_status(mx, my, cx, cy, t):
            nonlocal rows, cols
            res = []
            if t == 1:
                for i, j in directions:
                    for k in range(catJump+1):
                        row, col = cx+i*k, cy+j*k
                        if row < 0 or row >= rows or col < 0 or col >= cols:
                            continue
                        if grid[row][col] == '#':
                            break
                        res.append((mx, my, row, col, 2))
            else:
                for i, j in directions:
                    for k in range(mouseJump+1):
                        row, col = mx+i*k, my+j*k
                        if row < 0 or row >= rows or col < 0 or col >= cols:
                            continue
                        if grid[row][col] == '#':
                            break
                        res.append((row, col, cx, cy, 1))
            return res

        def is_all_next_win(mx, my, cx, cy, t):
            nonlocal rows, cols
            if t == 1:
                for i, j in directions:
                    for k in range(mouseJump+1):
                        row, col = mx + i * k, my + j * k
                        if row < 0 or row >= rows or col < 0 or col >= cols:
                            continue
                        if grid[row][col] == '#':
                            break
                        if (row,col,cx,cy,2) not in status or status[(row,col,cx,cy,2)] != 2:
                            return False
            else:
                for i, j in directions:
                    for k in range(catJump+1):
                        row, col = cx+i*k, cy+j*k
                        if row < 0 or row >= rows or col < 0 or col >= cols:
                            continue
                        if grid[row][col] == '#':
                            break
                        if (mx,my,row,col,1) not in status or status[(mx,my,row,col,1)] != 1:
                            return False
            return True

        while queue:
            step += 1
            if step > 2000:
                break
            l = len(queue)
            while l:
                l -= 1
                mx,my,cx,cy,t = queue.popleft()
                s = status[(mx,my,cx,cy,t)]

                for nmx, nmy, ncx, ncy, nt in find_prev_status(mx,my,cx,cy,t):
                    if (nmx, nmy, ncx, ncy, nt) in status:
                        continue
                    if nt == s:
                        status[(nmx, nmy, ncx, ncy, nt)] = s
                        queue.append((nmx, nmy, ncx, ncy, nt))
                    elif is_all_next_win(nmx, nmy, ncx, ncy, nt):
                        status[(nmx, nmy, ncx, ncy, nt)] = 3 - nt
                        queue.append((nmx, nmy, ncx, ncy, nt))

        return (mouse[0],mouse[1],cat[0], cat[1],1) in status and status[(mouse[0],mouse[1],cat[0], cat[1],1)] == 1


