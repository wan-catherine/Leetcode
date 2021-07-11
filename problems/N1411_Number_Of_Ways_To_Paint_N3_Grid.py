"""
use the column to do dp.
For each column, there are two situations:
    1. 3 colors for 3 cells
    2. 2 colors for 3 cells

Then for the first column :
    1. 3 colors has 6 different situations
    2. 2 colors has 6 different situations

then for dp[i+1], we can calculate for one 3-colors, we can get how many 3-colors and 2-colors,
we can also calculate for one 2-colors, we can get how many 3-colors and 2-colors.

for 2 colors :
aba -> bab, cbc, bcb (3 2-colors) , bac,cab (2 3-colors)
for 3 colors:
abc ->  bab, bcb (2 2-colors), bca, cab (2 3-colors)

then the dp formula is :
 three = previous_three * 2 + previous_two * 2
 two = previous_three * 2 + previous_two * 3
"""

class Solution:
    def numOfWays(self, n: int) -> int:
        m = 10 ** 9 + 7
        two, three = 6, 6
        for i in range(1, n):
            temp = three
            three = three * 2 + two * 2
            two = temp * 2 + two * 3
        return (two + three) % m