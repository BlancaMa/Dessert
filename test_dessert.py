from unittest import TestCase
import unittest
import dessert
import recommend
import data


class TestCases(unittest.TestCase):

    def test_find_by_flavor(self):
       self.fail()


    #def test_find_by_flavor_1(self):
        #input1 = "vanilla"
        #result = self.manager.find_by_flavor(input1)
        #expected = ["Vanilla Cake", "Vanilla Ice Cream"]
        #self.assertEqual(expected, [d.name for d in result])

    #def test_find_by_flavor_1(self):
        #input1 = "vanilla"
        #result = recommend.find_by_flavor(input1)
        #expected = ["Vanilla Cake", "Vanilla Ice Cream", "Creme Brulee"]
        #self.assertEqual(expected, [d.name for d in result])

    def test_find_by_flavor_found(self):
        result = recommend.find_by_flavor(dessert, "vanilla")
        expected = ["Vanilla Cake", "Vanilla Ice Cream", "Creme Brulee"]
        self.assertEqual(result, expected)

    def test_find_by_flavor_not_found(self):
        result = recommend.find_by_flavor(dessert, "mint")
        self.assertEqual(result, [])

    def test_find_by_texture_found(self):
        result = recommend.find_by_texture(dessert, "creamy")
        expected = ["Vanilla Ice Cream", "Chocolate Mousse", "Creme Brulee"]
        self.assertEqual([d["name"] for d in result], expected)

    def test_find_by_texture_not_found(self):
        result = recommend.find_by_texture(dessert, "fluffy")
        self.assertEqual(result, [])

    def test_find_by_cuisine_found(self):
        result = recommend.find_by_cuisine(dessert, "French")
        expected = ["Chocolate Mousse", "Creme Brulee"]
        self.assertEqual([d["name"] for d in result], expected)

    def test_find_by_cuisine_not_found(self):
        result = recommend.find_by_cuisine(dessert, "Italian")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()