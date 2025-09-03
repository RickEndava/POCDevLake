import unittest
from src.app import greet, add, multiply
import logging
import io
from contextlib import redirect_stderr

class TestApp(unittest.TestCase):
    def test_greet(self):
        """Test the greet function with different languages."""
        self.assertEqual(
            greet("World"),
            "Hello, World! Welcome to DevLake Demo Project for Endava"
        )
        self.assertEqual(
            greet("World", "es"),
            "¡Hola, World! Bienvenido al Proyecto Demo de DevLake para Endava"
        )
        self.assertEqual(
            greet("World", "fr"),
            "Bonjour, World ! Bienvenue au projet de démonstration DevLake pour Endava"
        )
        # Test unsupported language with warning
        with redirect_stderr(io.StringIO()) as stderr:
            result = greet("World", "de")
            self.assertEqual(
                result,
                "Hello, World! Welcome to DevLake Demo Project for Endava"
            )
            self.assertIn("Language 'de' not supported", stderr.getvalue())

    def test_add(self):
        """Test the add function with valid and invalid inputs."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)
        with self.assertRaises(ValueError):
            add("2", 3)
        with self.assertRaises(ValueError):
            add(2, "3")

    def test_multiply(self):
        """Test the multiply function with valid and invalid inputs."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5.0)
        with self.assertRaises(ValueError):
            multiply("2", 3)
        with self.assertRaises(ValueError):
            multiply(2, "3")

if __name__ == "__main__":
    unittest.main()