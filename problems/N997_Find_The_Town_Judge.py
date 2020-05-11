class Solution:
    def findJudge(self, N: int, trust) -> int:
        if N == 1 and not trust:
            return 1
        trust_map = {}
        non_judge = set()
        for t in trust:
            non_judge.add(t[0])
            trust_map.setdefault(t[1], set()).add(t[0])
        if len(non_judge) != N-1:
            return -1

        persons = set(trust_map.keys()) - non_judge
        if not persons or len(persons) != 1:
            return -1
        person = persons.pop()
        if trust_map[person] != non_judge:
            return -1
        return person