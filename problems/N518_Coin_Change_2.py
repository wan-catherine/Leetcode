class Solution:
    def change(self, amount, coins):
        db_table = [[1] + [0] * amount]
        for index in range(len(coins)):
            row = [1]
            for col in range(amount):
                used, unused = 0, 0
                if col + 1 - coins[index] >= 0:
                    used = row[col + 1 - coins[index]]
                unused = db_table[index][col + 1]
                row.append(used + unused)
            db_table.append(row)
        return db_table[-1][-1]