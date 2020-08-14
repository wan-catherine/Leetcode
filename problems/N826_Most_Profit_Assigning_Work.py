class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        difficulty_profit_mapping = {}
        difficulty_length = len(difficulty)
        for i in range(difficulty_length):
            if difficulty[i] not in difficulty_profit_mapping:
                difficulty_profit_mapping[difficulty[i]] = profit[i]
            else:
                difficulty_profit_mapping[difficulty[i]] = max(profit[i], difficulty_profit_mapping[difficulty[i]])

        difficulty.sort()
        for i in range(1, difficulty_length):
            difficulty_profit_mapping[difficulty[i]] = max(difficulty_profit_mapping[difficulty[i]], difficulty_profit_mapping[difficulty[i-1]])

        worker.sort()
        length = len(worker)
        res = 0
        d_index, w_index = 0, 0
        while d_index < difficulty_length and w_index < length:
            if difficulty[d_index] == worker[w_index]:
                res += difficulty_profit_mapping[difficulty[d_index]]
                w_index += 1
            elif difficulty[d_index] < worker[w_index]:
                if d_index + 1 >= difficulty_length:
                    res += difficulty_profit_mapping[difficulty[d_index]]
                    w_index += 1
                else:
                    if difficulty[d_index + 1] > worker[w_index]:
                        res += difficulty_profit_mapping[difficulty[d_index]]
                        w_index += 1
                    else:
                        d_index += 1
            else:
                w_index += 1
        return  res



