from unittest import TestCase
from problems.N675_Cut_Off_Trees_For_Golf_Event import Solution

class TestSolution(TestCase):
    def test_cut_off_tree(self):
        self.assertEqual(6, Solution().cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))

    def test_cut_off_tree_1(self):
        self.assertEqual(-1, Solution().cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))

    def test_cut_off_tree_2(self):
        self.assertEqual(6, Solution().cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))

    def test_cut_off_tree_3(self):
        self.assertEqual(57, Solution().cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]))

    def test_cut_off_tree_4(self):
        self.assertEqual(202, Solution().cutOffTree([[4557,6199,7461,2554,6132,7471,7103,4290],[2034,2301,6733,6040,2603,5697,9541,6678],[7308,7368,9618,4386,6944,3923,4754,4294],[0,3016,7242,5284,6631,1897,1767,7603],[2228,0,3625,7713,2956,3264,3371,6124],[9195,7804,2787,0,4919,9304,5161,502]]))