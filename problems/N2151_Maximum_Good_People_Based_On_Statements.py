from typing import List

"""
We can't use the wrong way to check.
Because bin(8) == '0b1000', bin(1) == '0b1', arr = set([i for i in range(len(snu)) if snu[i] == '1']), will be same. 

"""
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        length = len(statements)
        # wrong way to check
        # def check(number):
        #     snu = bin(number)[2:]
        #     arr = set([i for i in range(len(snu)) if snu[i] == '1'])
        #     for i in arr:
        #         for j in range(length):
        #             if statements[i][j] == 0 and j in arr:
        #                 return False
        #             if statements[i][j] == 1 and j not in arr:
        #                 return False
        #     return True
        def check(number):
            for i in range(length):
                if number & (1 << i) == 0:
                    continue
                for j in range(length):
                    if statements[i][j] == 0 and number & (1 << j):
                        return False
                    if statements[i][j] == 1 and number & (1 << j) == 0:
                        return False
            return True
        res = 0
        for status in range(2**length):
            if check(status):
                res = max(res, bin(status).count('1'))
        return res