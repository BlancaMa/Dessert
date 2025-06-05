from unittest import TestCase
import unittest
import d1
import recommend
import data

#Blanca

class TestCases(unittest.TestCase):

    def test_get_input1(self):
        print("\nTest 1: Please enter 'vanilla' when prompted.")
        expected = "vanilla"
        result = recommend.get_input("Choose a flavor:", ["vanilla", "chocolate", "fruits", "mint", "Cookies and cream", "coffee", "cinnamon"])
        self.assertEqual(expected, result)

    def test_get_input2(self):
        print("\nTest 2: Please enter 'apple' (invalid), then 'chocolate' (valid).")
        expected = "chocolate"
        result = recommend.get_input("Choose a flavor:", ["vanilla", "chocolate", "fruits", "mint", "Cookies and cream", "coffee", "cinnamon"])
        self.assertEqual(expected, result)

    def test_recommend1(self):
        texture = "chewy"
        flavor = "chocolate"
        cuisine = "american"
        result = recommend.recommend_dessert(texture, flavor, cuisine)
        # The recommended dessert should contain "Brownie"
        self.assertIn("Brownie", result)

    def test_recommend2(self):
        texture = "hard"
        flavor = "mint"
        cuisine = "asian"
        result = recommend.recommend_dessert(texture, flavor, cuisine)
        expected = "Sorry, no desserts match your choices."
        self.assertEqual(expected, result)


    def test_main_manual_1(self):
        print("\nManual Test 1: Enter chewy, chocolate, american when prompted")
        recommend.main()


    def test_main_manual_2(self):
        print("\nManual Test 2: Enter smooth, mint, french (no match expected)")
        recommend.main()



if __name__ == "__main__":
    unittest.main()