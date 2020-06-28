from unittest import TestCase
from problems.N332_Reconstruct_Itinerary import Solution

class TestSolution(TestCase):
    def test_findItinerary(self):
        input = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        output = ["JFK", "MUC", "LHR", "SFO", "SJC"]
        self.assertListEqual(output, Solution().findItinerary(input))

    def test_findItinerary_1(self):
        input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        output = ["JFK","ATL","JFK","SFO","ATL","SFO"]
        self.assertListEqual(output, Solution().findItinerary(input))

    def test_findItinerary_2(self):
        input = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
        output = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
        self.assertListEqual(output, Solution().findItinerary(input))
