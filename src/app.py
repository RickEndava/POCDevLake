import logging

logging.basicConfig(level=logging.WARNING)

def greet(name, language="en"):
    """Return a greeting message in the specified language."""
    greetings = {
        "en": f"Hello, {name}! Welcome to DevLake Demo Project for Endava",
        "es": f"¡Hola, {name}! Bienvenido al Proyecto Demo de DevLake para Endava",
        "fr": f"Bonjour, {name} ! Bienvenue au projet de démonstration DevLake pour Endava"
    }
    return greetings.get(language, greetings["en"])  # Default to English if language not found

def add(a, b):
    """Add two numbers and return the result."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a * b

if __name__ == "__main__":
    # Test the greet function with different languages
    print(greet("DevLake"))  # Default: English
    print(greet("DevLake", "es"))  # Spanish
    print(greet("DevLake", "fr"))  # French
    
    # Test the add and multiply functions
    try:
        print(f"Sum: {add(5, 3)}")  # Should print 8
        print(f"Product: {multiply(5, 3)}")  # Should print 15
    except ValueError as e:
        print(f"Error: {e}")