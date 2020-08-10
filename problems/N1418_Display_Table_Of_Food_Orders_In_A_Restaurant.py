import collections


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        table_food_mapping = {}
        food_set = set()
        for _, table, food in orders:
            food_set.add(food)
            if table not in table_food_mapping:
                table_food_mapping[table] = {}
            if food not in table_food_mapping[table]:
                table_food_mapping[table][food] = 1
            else:
                table_food_mapping[table][food] += 1


        header = ['Table'] + sorted(food_set)
        res = [header]
        length = len(header)
        tables = sorted(table_food_mapping.keys(), key=lambda table : int(table))
        for t in tables:
            row = [str(t)]
            for i in range(1, length):
                if header[i] not in table_food_mapping[str(t)]:
                    row.append("0")
                else:
                    row.append(str(table_food_mapping[str(t)][header[i]]))

            res.append(row)
        return res
