def validate_ingredients(ingredients: str) -> str:
    lst = ["fire", "water", "earth", "air"]
    words = ingredients.split(" ")
    if all(word in lst for word in words):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
