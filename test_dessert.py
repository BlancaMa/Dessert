from unittest import TestCase
import unittest


class TestCases(unittest.TestCase):

    #def test_find_by_flavor(self):
       # self.fail()


    #def test_find_by_flavor_1(self):
        #input1 = "vanilla"
        #result = self.manager.find_by_flavor(input1)
        #expected = ["Vanilla Cake", "Vanilla Ice Cream"]
        #self.assertEqual(expected, [d.name for d in result])

    def test_find_by_flavor_1(self):
        input1 = "vanilla"
        result = self.find_by_flavor(input1)
        expected = ["Vanilla Cake", "Vanilla Ice Cream"]
        self.assertEqual(expected, [d.name for d in result])

    def test_find_by_texture_1(self):
        input1 = "creamy"
        result = self.manager.find_by_texture(input1)
        expected = ["Vanilla Ice Cream", "Chocolate Mousse"]
        self.assertEqual(expected, [d.name for d in result])

    def test_find_by_cuisine_1(self):
        input1 = "French"
        result = self.manager.find_by_cuisine(input1)
        expected = ["Creme Brulee"]
        self.assertEqual(expected, [d.name for d in result])