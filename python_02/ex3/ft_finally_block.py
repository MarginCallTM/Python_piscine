def water_plants(plants_list: list[str | None]) -> None:
    print("Opening watering system")
    try:
        for plant in plants_list:
            if plant is None:
                raise TypeError("Cannot water None - Invalid plant!")
            print(f"Watering {plant}")
    except TypeError as error:
        print(f"Error {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
