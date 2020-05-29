class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        self.row_len = len(votes[0])
        self.row_letter_mapping = {i:[0] * self.row_len for i in votes[0]}

        for vote in votes:
            for i in range(len(vote)):
                self.row_letter_mapping[vote[i]][i] += 1

        res = []
        self.sort_team(res, 0, list(votes[0]))
        return ''.join(res)

    def sort_team(self, res, position, teams):
        if position >= self.row_len:
            res += sorted(teams)
            return

        dict_position= {}
        for key in self.row_letter_mapping:
            if key in teams:
                dict_position.setdefault(self.row_letter_mapping[key][position], []).append(key)

        for p in sorted(dict_position, reverse=True):
            if len(dict_position[p]) == 1:
                res.append(dict_position[p][0])
            else:
                self.sort_team(res, position + 1, dict_position[p])




