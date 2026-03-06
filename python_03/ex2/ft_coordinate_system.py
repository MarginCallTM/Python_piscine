import sys
import math


class CoordinateSystem:
    def __init__(self) -> None:
        pass

    def claims_args(self, argv) -> None:
        if len(argv) == 2:
            return self.parse_coordinates(argv[1])
        if len(argv) < 4:
            print("Usage: python3 ft_coordinate_system.py <x> <y> <z>")
            return None
        try:
            x = int(argv[1])
            y = int(argv[2])
            z = int(argv[3])
            return (x, y, z)
        except ValueError as e:
            print(f"Error: coordinates must be numbers, got {e}")
            return None

    def create_position(self, x, y, z) -> tuple:
        return (x, y, z)

    def parse_coordinates(self, coord_str) -> tuple:
        try:
            parts = coord_str.split(",")
            x, y, z = parts
            return (int(x), int(y), int(z))
        except ValueError as e:
            print(f"Error parsing coorfinates: {e}")
            print(f"Error details - Type: ValueError, args: {e.args}")
            return None

    def calculate_distance(self, point1, point2) -> float:
        x1, y1, z1 = point1
        x2, y2, z2 = point2
        return round(math.sqrt((x2 - x1) ** 2 +
                     (y2 - y1)**2 + (z2 - z1)**2), 2)

    def unpack_demo(self, position) -> None:
        x, y, z = position
        print(f"Player at x= {x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    location = CoordinateSystem()

    position_from_args = location.claims_args(sys.argv)
    if position_from_args:
        print(f"Position created: {position_from_args}")
        origin = location.create_position(0, 0, 0)
        distance = location.calculate_distance(origin, position_from_args)
        print(
            f"Distance between {origin} and {position_from_args}: {distance}")
    print("\nUnpacking demonstration:")

    x, y, z = position_from_args

    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
