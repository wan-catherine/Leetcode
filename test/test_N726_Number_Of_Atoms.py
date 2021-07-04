from unittest import TestCase
from problems.N726_Number_Of_Atoms import Solution

class TestSolution(TestCase):
    def test_count_of_atoms(self):
        self.assertEqual("H2O", Solution().countOfAtoms("H2O"))

    def test_count_of_atoms_1(self):
        self.assertEqual("H2MgO2", Solution().countOfAtoms("Mg(OH)2"))

    def test_count_of_atoms_2(self):
        self.assertEqual("K4N2O14S4", Solution().countOfAtoms("K4(ON(SO3)2)2"))

    def test_count_of_atoms_3(self):
        self.assertEqual("Be32", Solution().countOfAtoms("Be32"))

    def test_count_of_atoms_4(self):
        self.assertEqual("H2MgNO", Solution().countOfAtoms("Mg(H2O)N"))
