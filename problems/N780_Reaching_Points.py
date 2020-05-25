class Solution(object):
    #RuntimeError: maximum recursion depth exceeded
    def reachingPoints_slow(self, sx, sy, tx, ty):
        if sx == tx and sy == ty:
            return True
        if sx > tx or sy > ty:
            return False
        left = self.reachingPoints(sx+sy,sy, tx, ty)
        right = self.reachingPoints(sx,sx+sy, tx,ty)

        return left or right

    # check tx, ty
    # because there is only two changes : x,y --> x+y,y or x,x+y
    # if tx > ty : then the very last change should be (x+y, y) , then we can get (tx-ty, ty)
    # if tx <= ty : then the very last change should be (x, x+y), then we can get (tx, ty-tx)
    # about tx == ty, you can put in any of the change . 
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if sx == tx:
                return (ty - sy) % sx == 0
            if sy == ty:
                return (tx - sx) % sy == 0
            if tx > ty:
                tx = tx - ty
                continue
            if tx <= ty:
                ty = ty - tx
                continue
        return False
