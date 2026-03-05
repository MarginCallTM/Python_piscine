class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class FarmerError(GardenError):
    pass


def check_plant(name, status):
    if status == "wilting":
        raise PlantError(f"The {name} plant is wilting!")
    if status == "dead":
        raise PlantError(f"The {name} plant is dead!")


def check_water(tank_level):
    if tank_level < 10:
        raise WaterError("Not enought water in the tank!")


def test_error_types():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        check_water(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    operations = [
        lambda: check_plant("tomato", "wilting"),
        lambda: check_water(5),
    ]
    for operation in operations:
        try:
            operation()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
