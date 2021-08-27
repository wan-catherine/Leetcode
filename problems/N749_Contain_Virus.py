from typing import List

"""
copy the code directly .
"""

class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def cells():
            for r in range(R):
                for c in range(C):
                    yield (r, c)

        def is_valid(i, j):
            return 0 <= i < R and 0 <= j < C

        def neighbours(r, c):
            """Get valid neighbour cells"""
            for dr, dc in dirs:
                if is_valid(r + dr, c + dc):
                    yield (r + dr, c + dc)

        def pick_most_threatening_region():
            visited = set()

            def dfs(r, c):
                """Returns number of walls needed to quarantine infected region
                starting at (r,c)"""
                # Avoid already visited or quarantined cells.
                if (r, c) in visited or grid[r][c] == -1:
                    return 0
                # Found an empty perimeter space
                if grid[r][c] == 0:
                    perimeter.add((r, c))
                    # Counts as one wall needed to contain infected cell.
                    return 1

                visited.add((r, c))
                # Explore neighbours and return the sum of the walls needed to
                # contain their perimeter.
                return sum(dfs(nr, nc) for (nr, nc) in neighbours(r, c))

            max_perimeter, max_p_walls, max_start = 0, 0, (0, 0)
            for r, c in cells():
                # Find cells that have not yet been visited and are infected.
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter = set()
                    # Get the total walls needed to quarantine the infected region.
                    walls = dfs(r, c)
                    # If the parameter we could save is the biggest we've seen...
                    if len(perimeter) > max_perimeter:
                        # update the walls needed to quarantine, and an infected cell
                        # from which we might mark the infected region as quarantined (setting -1)
                        max_perimeter, max_p_walls, max_start = len(perimeter), walls, (r, c)
            return max_p_walls, max_start

        def quarantine(r, c):
            """Mark an infected region as quarantined by setting cells to -1"""
            grid[r][c] = -1
            # Explore neighbours to quarantine them too.
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    quarantine(nr, nc)

        def simulate_night():
            """Spreads the infection by one night of non-quarntined regions."""

            def infected_neighbour(r, c):
                """Returns True if an orthogonally adjacent square is infected."""
                return any(grid[nr][nc] == 1 for nr, nc in neighbours(r, c))

            for r, c in cells():
                # Find clean cells that are next to infected cells
                if grid[r][c] == 0 and infected_neighbour(r, c):
                    # Set them temporarily to 2, so that further iterations do not
                    # count them as infected (otherwise it would spread endlessly
                    # in one night).
                    grid[r][c] = 2

            # Go over a second time and set the temporarily marked newly infected cells
            # to permanently infected.
            for r, c in cells():
                if grid[r][c] == 2:
                    grid[r][c] = 1

        if not grid or not grid[0]:
            return 0
        R, C = len(grid), len(grid[0])

        walls = 0
        while True:
            new_walls, (r, c) = pick_most_threatening_region()
            # Stop when there are no more infected regions, i.e. only
            # -1 (quarantined by us) and 0's are left.
            if new_walls == 0:
                return walls
            quarantine(r, c)
            walls += new_walls
            simulate_night()
        return walls