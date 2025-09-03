import logging
import sys

# Configurar logging para enviar advertencias a stderr
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.handlers = []  # Limpiar handlers por defecto
logger.addHandler(logging.StreamHandler(sys.stderr))

def greet(name, language="en"):
    """Return a greeting message in the specified language."""
    greetings = {
        "en": f"Hello, {name}! Welcome to DevLake Demo Project for Endava",
        "es": f"¡Hola, {name}! Bienvenido al Proyecto Demo de DevLake para Endava",
        "fr": f"Bonjour, {name} ! Bienvenue au projet de démonstration DevLake pour Endava"
    }
    if language not in greetings:
        logger.warning(f"Language '{language}' not supported, defaulting to English")
    return greetings.get(language, greetings["en"])

def add(a, b):
    """Add two numbers and return the result."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    if a is None or b is None:
        raise ValueError("Both arguments must be numbers, got None")
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a * b

if __name__ == "__main__":
    # Test the greet function with different languages
    print(greet("DevLake"))  # Default: English
    print(greet("DevLake", "es"))  # Spanish
    print(greet("DevLake", "fr"))  # French
    print(greet("DevLake", "de"))  # Unsupported language
    
    # Test the add and multiply functions
    try:
        print(f"Sum: {add(5, 3)}")  # Should print 8
        print(f"Product: {multiply(5, 3)}")  # Should print 15
        print(f"Test invalid input: {add('invalid', 3)}")  # Should raise ValueError
    except ValueError as e:
        logger.error(f"Error in main block: {e}")
        print(f"Error: {e}")