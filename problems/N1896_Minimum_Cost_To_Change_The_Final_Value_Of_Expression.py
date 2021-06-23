class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        def eval_value(opt, left, right):
            if opt == '#':
                return right[0]
            if opt == '&':
                return left[0] & right[0]
            else:
                return left[0] | right[0]

        def eval_flip(opt, left, right):
            if opt == '#':
                return right[1]
            if opt == '&':
                if left[0] + right[0] == 2:
                    return min(left[1], right[1])
                elif left[0] + right[0] == 1:
                    return 1
                else:
                    return min(left[1], right[1]) + 1
            else:
                if left[0] + right[0] == 2:
                    return min(left[1], right[1]) + 1
                elif left[0] + right[0] == 1:
                    return 1
                else:
                    return min(left[1], right[1])

        nums, opts = [], []
        opt, cur = '#', -1
        for c in expression:
            if c in '&|':
                opt = c
            elif c in '01':
                next = [ord(c) - ord('0'), 1]
                val = eval_value(opt, cur, next)
                flip = eval_flip(opt, cur, next)
                cur = [val, flip]
            elif c == '(':
                nums.append(cur)
                opts.append(opt)
                cur, opt = [-1, -1], '#'
            else:
                last = nums.pop()
                opt = opts.pop()
                val = eval_value(opt, last, cur)
                flip = eval_flip(opt, last, cur)
                cur = [val, flip]
        return cur[1]