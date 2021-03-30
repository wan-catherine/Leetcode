from unittest import TestCase
from problems.N864_Shortest_Path_To_Get_All_Keys import Solution

class TestSolution(TestCase):
    def test_shortest_path_all_keys(self):
        self.assertEqual(8, Solution().shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))

    def test_shortest_path_all_keys_1(self):
        self.assertEqual(6, Solution().shortestPathAllKeys(["@..aA","..B#.","....b"]))

    def test_shortest_path_all_keys_2(self):
        self.assertEqual(-1, Solution().shortestPathAllKeys(["@Aa"]))

    def test_shortest_path_all_keys_3(self):
        self.assertEqual(10, Solution().shortestPathAllKeys(["@...a",".###A","b.BCc"]))
