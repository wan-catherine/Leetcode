"""
dpij :
    1. i: there are i 'A' for last two records (0, 1)
    2. j : there are j 'L' for last two records (0, 1, 2)
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        dp00, dp01, dp02, dp10, dp11, dp12 = 1, 0, 0, 0, 0, 0
        m = 10 ** 9 + 7
        for i in range(1, n + 1):
            old_dp00, old_dp01, old_dp02, old_dp10, old_dp11, old_dp12 = dp00, dp01, dp02, dp10, dp11, dp12
            dp00 = (old_dp00 + old_dp01 + old_dp02) % m
            dp01 = old_dp00 % m
            dp02 = old_dp01 % m
            dp10 = (old_dp00 + old_dp01 + old_dp02 + old_dp10 + old_dp11 + old_dp12) % m
            dp11 = old_dp10 % m
            dp12 = old_dp11 % m
        return sum([dp00, dp01, dp02, dp10, dp11, dp12]) % m
