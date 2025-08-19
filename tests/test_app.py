import unittest
from src.app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
            result = greet("World")
            self.assertIn("Hello, World", result)



if __name__ == "__main__":
    unittest.main()
