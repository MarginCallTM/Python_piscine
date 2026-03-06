def garden_operations(operation: str, user_input: str = "") -> None:
    if operation == "value":
        _ = int(user_input)
    elif operation == "zero":
        try:
            _ = 10 / int(user_input)
        except ValueError:
            print(f"'{user_input}' is not a valid number")
    elif operation == "file":
        with open(user_input) as f:
            _ = f.read()
    elif operation == "key":
        plants = {"rose": "red", "tulip": "yellow", "lily": "white"}
        _ = plants[user_input]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value", "string")
    except ValueError as error:
        print(f"Caught ValueError: {error}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero", "0")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file", "missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key", "'missing\\_plant'")
    except KeyError as error:
        print(f"Caught KeyError: {error.args[0]}")
    print()

    print("Testing multiple errors together...")
    for op, data in [("value", "abc"), ("zero", "0")]:
        try:
            garden_operations(op, data)
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")
            break
    print("\nAll error types tested successfully")


if __name__ == "__main__":
    test_error_types()
