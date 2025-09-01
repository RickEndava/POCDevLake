def greet(name, language="en"):
    greetings = {
        "en": f"Hello, {name}! Welcome to DevLake Demo Project for Endava",
        "es": f"¡Hola, {name}! Bienvenido al Proyecto Demo de DevLake para Endava"
    }
    return greetings.get(language, greetings["en"])

def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers")
    return a + b

if __name__ == "__main__":
    print(greet("DevLake"))
    print(greet("DevLake", "es"))

