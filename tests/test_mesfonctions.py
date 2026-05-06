import unittest
from mesfonctions import addition, soustraction, multiplication, pair, factorielle


class TestMesFonctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_pair(self):
        self.assertTrue(pair(8))
        self.assertFalse(pair(7))

    def test_factorielle(self):
        self.assertEqual(factorielle(5), 120)


if __name__ == "__main__":
    unittest.main()
