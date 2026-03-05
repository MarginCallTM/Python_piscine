def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(
                f"{temp} is too cold for plants (min 0°C)"
            )
        if temp > 40:
            raise ValueError(
                f"{temp} is too hot for plants (max 40°C)"
            )
        return temp
    except ValueError as error:
        if "too hot" in str(error) or "too cold" in str(error):
            print(f"Error: {error}")
        else:
            print(f"{temp_str} is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-5000"]

    for value in test_values:
        print(f"Testing temperature {value}")

        result = check_temperature(value)

        if result is not None:
            print(f"Temperature {value}°C is perfect for plants!")

        print()
    print("All test are complete")


if __name__ == "__main__":
    test_temperature_input()
