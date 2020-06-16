from unittest import TestCase
from problems.N468_Validate_IP_Address import Solution

class TestSolution(TestCase):
    def test_validIPAddress(self):
        self.assertEqual('IPv4', Solution().validIPAddress("172.16.254.1"))

    def test_validIPAddress_1(self):
        self.assertEqual("IPv6", Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))

    def test_validIPAddress_2(self):
        self.assertEqual('Neither', Solution().validIPAddress("256.256.256.256"))

    def test_validIPAddress_3(self):
        self.assertEqual("IPv6", Solution().validIPAddress("2001:0db8:85a3:0000:0:8A2E:0370:733a"))

    def test_validIPAddress_4(self):
        self.assertEqual("Neither", Solution().validIPAddress("2001:0db8:85a3:00000:0:8A2E:0370:7334"))

    def test_validIPAddress_5(self):
        self.assertEqual("Neither", Solution().validIPAddress("3204989084338912748932647812689708923sdjlkch9 i389273012380009832437218947389-7534iodu"))