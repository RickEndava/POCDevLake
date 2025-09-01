# tests/test_app.py
import unittest
from src.app import greet, add, multiply

class TestApp(unittest.TestCase):
    def test_greet(self):
        """Test the greet function with different languages."""
        # Test default language (English)
        self.assertEqual(
            greet("World"),
            "Hello, World! Welcome to DevLake Demo Project for Endava"
        )
        # Test Spanish
        self.assertEqual(
            greet("World", "es"),
            "¡Hola, World! Bienvenido al Proyecto Demo de DevLake para Endava"
        )
        # Test French
        self.assertEqual(
            greet("World", "fr"),
            "Bonjour, World ! Bienvenue au projet de démonstration DevLake pour Endava"
        )
        # Test invalid language (should default to English)
        self.assertEqual(
            greet("World", "de"),
            "Hello, World! Welcome to DevLake Demo Project for Endava"
        )

    def test_add(self):
        """Test the add function with valid and invalid inputs."""
        # Test valid inputs
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)  # Test with floats
        # Test invalid inputs
        with self.assertRaises(ValueError):
            add("2", 3)
        with self.assertRaises(ValueError):
            add(2, "3")

    def test_multiply(self):
        """Test the multiply function with valid and invalid inputs."""
        # Test valid inputs
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5.0)  # Test with floats
        # Test invalid inputs
        with self.assertRaises(ValueError):
            multiply("2", 3)
        with self.assertRaises(ValueError):
            multiply(2, "3")

if __name__ == "__main__":
    unittest.main()