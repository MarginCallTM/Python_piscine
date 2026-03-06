class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, name: str) -> None:
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plants[name] = {"water": 0, "sun": 0}

    def water_plant(self) -> None:
        print("Opening watering system")
        try:
            for name in self.plants:
                print(f"Watering {name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def validate_inputs(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("Plant name must be a non-empty string!")
        if not isinstance(water_level, int):
            raise ValueError(
                f"Water level must be a number, got '{water_level}'"
            )
        if not isinstance(sunlight_hours, int):
            raise ValueError(
                f"Sunlight hours must be a number, got '{sunlight_hours}'"
            )

    def check_health(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> str:
        self.validate_inputs(name, water_level, sunlight_hours)
        if water_level > 10:
            raise ValueError(
                f"Water level {water_level} is too high (max 10)"
            )
        if water_level < 1:
            raise ValueError(
                f"Water level {water_level} is too low (min 1)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        return f"{name}: healthy (Water: {water_level}, sun: {sunlight_hours})"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager()

    print("Adding plant to garden...")
    for name in ["tomato", "lettuce", ""]:
        try:
            garden.add_plant(name)
            print(f"Added {name} successfully")
        except ValueError as error:
            print(f"Error adding plant: {error}")

    print("\nWatering plants...")
    garden.water_plant()

    print("\nChecking plant health...")
    checks = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
    ]
    for name, water, sun in checks:
        try:
            result = garden.check_health(name, water, sun)
            print(result)
        except ValueError as error:
            print(f"Error checking {name}: {error}")

    print("\nTesting error recovery")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
