from unittest import TestCase
import unittest

class TestDessertManager(unittest.TestCase):

    def test_find_by_flavor(self):
        self.fail()


    def test_find_by_flavor_1(self):
        input1 = "vanilla"
        result = self.manager.find_by_flavor(input1)
        expected = ["Vanilla Cake", "Vanilla Ice Cream"]
        self.assertEqual(expected, [d.name for d in result])

