from unittest import TestCase
from problems.N1964_Find_The_Longest_Valid_Obstacle_Course_At_Each_Position import Solution

class TestSolution(TestCase):
    def test_longest_obstacle_course_at_each_position(self):
        self.assertListEqual([1,2,3,3], Solution().longestObstacleCourseAtEachPosition([1,2,3,2]))

    def test_longest_obstacle_course_at_each_position_1(self):
        self.assertListEqual([1,2,1], Solution().longestObstacleCourseAtEachPosition([2,2,1]))

    def test_longest_obstacle_course_at_each_position_2(self):
        self.assertListEqual([1,1,2,3,2,2], Solution().longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))
