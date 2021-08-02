from typing import List
"""
we only need to consider the largest task : 
ABD
ABD
ABE
AB
AC
AC
AC
A
A
"""

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        total = sum(milestones)
        if milestones[-1] > total // 2:
            return (total - milestones[-1]) * 2 + 1
        return total