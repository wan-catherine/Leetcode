from unittest import TestCase
from problems.N735_Asteroid_Collision import Solution

class TestSolution(TestCase):
    def test_asteroidCollision(self):
        self.assertListEqual([5, 10], Solution().asteroidCollision([5, 10, -5]))

    def test_asteroidCollision_1(self):
        self.assertListEqual([], Solution().asteroidCollision([8, -8]))

    def test_asteroidCollision_2(self):
        self.assertListEqual([10], Solution().asteroidCollision([10, 2, -5]))

    def test_asteroidCollision_3(self):
        self.assertListEqual([-2, -1, 1, 2], Solution().asteroidCollision([-2, -1, 1, 2]))

    def test_asteroidCollision_4(self):
        self.assertListEqual([-2,-2,-2], Solution().asteroidCollision([-2,-2,1,-2]))

    def test_asteroidCollision_5(self):
        self.assertListEqual([-2,-2], Solution().asteroidCollision([-2,-2,1,-1]))

    def test_asteroidCollision_6(self):
        self.assertListEqual([-2,-2,-2], Solution().asteroidCollision([1,-2,-2,-2]))
