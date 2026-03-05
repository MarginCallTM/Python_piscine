def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low! (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high! (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as error:
        print(f"Error : {error}")

    print("\nTesting with empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nTesting with bad water level...")
    try:
        check_plant_health("lettuce", 15, 8)
    except ValueError as error:
        print(f"Error : {error}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 1)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
