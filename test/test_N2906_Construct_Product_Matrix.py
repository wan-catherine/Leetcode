from unittest import TestCase
from problems.N2906_Construct_Product_Matrix import Solution

class TestSolution(TestCase):
    def test_construct_product_matrix(self):
        self.assertListEqual([[24,12],[8,6]], Solution().constructProductMatrix([[1,2],[3,4]]))

    def test_construct_product_matrix_1(self):
        self.assertListEqual([[2],[0],[0]], Solution().constructProductMatrix([[12345],[2],[1]]))

    def test_construct_product_matrix_2(self):
        self.assertListEqual([[615,7095,7776],[6480,9720,615],[6480,615,1845]], Solution().constructProductMatrix([[3,2,5],[6,4,3],[6,3,1]]))
