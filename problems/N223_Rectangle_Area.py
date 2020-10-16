class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        left = max(A, E)
        right = max(min(C, G), left)
        bottom = max(B, F)
        top = max(min(D, H), bottom)

        return abs(A-C)*abs(B-D) + abs(E-G)*abs(F-H) - (right-left)*(top-bottom)

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a = [A, B, C, D]
        b = [E, F, G, H]

        left_x = max(a[0], b[0])
        right_x = min(a[2], b[2])
        up_y = min(a[3], b[3])
        down_y = max(a[1], b[1])

        overlap = 0
        if left_x < right_x and up_y > down_y:
            overlap = (right_x - left_x) * (up_y - down_y)

        area = 0
        area += (C - A) * (D - B)
        area += (G - E) * (H - F)

        return area - overlap
