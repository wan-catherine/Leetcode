from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = '(' + s + ')'
        length = len(s)
        opts, nums = [], []
        i = 0
        nidx, oindx = [], []
        while i < length:
            if s[i] in '(+-*/':
                if s[i] == '(':
                    nidx.append(len(nums))
                    oindx.append(len(opts))
                opts.append(s[i])
            elif s[i] == ')':
                ni, no = nidx.pop(), oindx.pop()
                ndq = deque(nums[ni:])
                odq = deque(opts[no+1:])
                while len(ndq) > 1:
                    left, right = ndq.popleft(), ndq.popleft()
                    opt = odq.popleft()
                    if opt == '+':
                        ndq.appendleft(left + right)
                    elif opt == '-':
                        ndq.appendleft(left - right)
                    else:
                        print('error')
                nums = nums[:ni]
                opts = opts[:no]
                nums.append(ndq[0])
                while opts and opts[-1] in '*/':
                    opt = opts.pop()
                    right, left = nums.pop(), nums.pop()
                    if opt == '*':
                        nums.append(left * right)
                    else:
                        nums.append(left // right if left * right >= 0 else left // right + 1)
            else:
                v = 0
                while i < length and s[i].isdigit():
                    v *= 10
                    v += int(s[i])
                    i += 1
                i -= 1
                if opts and opts[-1] in '*/':
                    opt = opts.pop()
                    left = nums.pop()
                    if opt == '*':
                        nums.append(left * v)
                    else:
                        if left * v < 0:
                            nums.append(left // v + 1)
                        else:
                            nums.append(left // v)
                else:
                    nums.append(v)
            i += 1
        return nums[0]
