import unittest
from src.app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
            self.assertEqual(greet("World"), "Hello, World! Welcome to DevLake Demo Project for Endava")


if __name__ == "__main__":
    unittest.main()
