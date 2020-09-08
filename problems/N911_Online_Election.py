import bisect
import collections


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times
        self.length = len(self.persons)
        mapping = collections.defaultdict(int)
        self.status = []
        prev = [-1, 0]
        for index, person in enumerate(self.persons):
            mapping[person] += 1
            if mapping[person] > prev[1]:
                self.status.append(person)
                prev[0],prev[1] = person, mapping[person]
            elif mapping[person] < prev[1]:
                self.status.append(prev[0])
            else:
                self.status.append(person)
                prev[0] = person

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        index = bisect.bisect_left(self.times, t)
        if index == 0 or (index < self.length and self.times[index] == t):
            return self.status[index]

        return self.status[index - 1]

# ["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"]
# [[],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]

obj = TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])
print(obj.q(45))
print(obj.q(49))
print(obj.q(59))
print(obj.q(68))
print(obj.q(42))
print(obj.q(37))

print(obj.q(99))
print(obj.q(26))
print(obj.q(78))
print(obj.q(43))
