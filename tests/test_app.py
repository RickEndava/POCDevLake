import unittest
from src.app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
            result = greet("World")
            self.assertIn("Hello, World", result)
    
    def test_add(self):
         self.assertEqual(add(2, 3), 5)




if __name__ == "__main__":
    unittest.main()
