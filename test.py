from asker import *
import unittest

class TestQuestions(unittest.TestCase):

    def testAddInt(self):
        self.assertEqual(addInt(17, 24), 41)

    def testSubtractInt(self):
        self.assertEqual(subtract(45, 18), 27)

    def testMultiplyInt(self):
        self.assertEqual(multiply(7, 3), 21)

    def testDecimals(self):
        self.assertEqual(addFloat(-2.4, 1.7), -0.7)

    def testFractions(self):
        """Test questions on fractions"""
        pass

if __name__ == "__main__":
    unittest.main()

