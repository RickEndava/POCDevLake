def greet(name, language="en"):
    greetings = {
        "en": f"Hello, {name}! Welcome to DevLake Demo Project for Endava",
        "es": f"¡Hola, {name}! Bienvenido al Proyecto Demo de DevLake para Endava"
    }
    return greetings.get(language, greetings["en"])
#Adding this feature branch
if __name__ == "__main__":
    print(greet("DevLake"))
    print(greet("DevLake", "es"))