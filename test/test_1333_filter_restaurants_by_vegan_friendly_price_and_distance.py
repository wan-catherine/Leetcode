from unittest import TestCase
from problems.N1333_Filter_Restaurants_By_Vegan_Friendly_Price_And_Distance import Solution

class TestSolution(TestCase):
    def test_filterRestaurants(self):
        restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3],
                       [5, 1, 1, 15, 1]]
        veganFriendly = 1
        maxPrice = 50
        maxDistance = 10
        self.assertListEqual([3,1,5], Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))

    def test_filterRestaurants_1(self):
        restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
        veganFriendly = 0
        maxPrice = 50
        maxDistance = 10
        self.assertListEqual([4,3,2,1,5], Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))

    def test_filterRestaurants_2(self):
        restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
        veganFriendly = 0
        maxPrice = 30
        maxDistance = 3
        self.assertListEqual([4,5], Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))
