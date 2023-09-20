"""
AABBAABBAA
BBAABBAABB
AABBAABB

Then AB can be in BB...AA
BBz...zAA
"""
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (min(x,y) * 2 + z + min(1, abs(x-y))) * 2