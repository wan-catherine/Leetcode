from unittest import TestCase
from problems.N1418_Display_Table_Of_Food_Orders_In_A_Restaurant import Solution

class TestSolution(TestCase):
    def test_displayTable(self):
        orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                  ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
        output = [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
        self.assertListEqual(output, Solution().displayTable(orders))

    def test_displayTable_1(self):
        orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
        output = [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
        self.assertListEqual(output, Solution().displayTable(orders))

    def test_displayTable_2(self):
        orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
        output = [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
        self.assertListEqual(output, Solution().displayTable(orders))
