import unittest
from calculator import add # type: ignore # Import the functions to test

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Check if 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0) # Check negative numbers
        self.assertEqual(add(0, 0), 0)  # Check zero case

# Run the tests
if __name__ == "__main__":
    unittest.main()