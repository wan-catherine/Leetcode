from unittest import TestCase
from problems.N1257_Smallest_Common_Region import Solution

class TestSolution(TestCase):
    def test_findSmallestRegion(self):
        self.assertEqual("North America", Solution().findSmallestRegion(regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"))
