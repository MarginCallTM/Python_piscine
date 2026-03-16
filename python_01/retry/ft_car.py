class car:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount: int) -> None:
        self.speed += amount
        print(f"{self.speed}km/h")

    def brake(self, power: int) -> None:
        self.speed -= power
        actual_speed = self.speed
        if actual_speed > 0:
            print(f"{actual_speed} km/h")
        elif actual_speed <= 0:
            print("car stopped")

    def get_info(self) -> None:
        print(f"[{self.brand}] Speed: {self.speed}km/h")


class elec_car(car):
    def __init__(self, brand: str, battery: int) -> None:
        super().__init__(brand)
        self.battery = 100

    def accelerate_test(self, amount: int) -> None:
        self.battery -= 5
        battery_level = self.battery
        if battery_level <= 0:
            print("Car out of battery")
        elif battery_level >= 0:
            print(f"Car battery level {battery_level}")

    def get_info(self) -> None:
        print(f"[{self.brand}] Battery level: {self.battery}%")


if __name__ == "__main__":
    toyota = car("toyota")
    tesla = elec_car("Tesla", 100)
    tesla.accelerate(9)
    toyota.accelerate(50)
    toyota.brake(50)
    toyota.get_info()

    tesla.accelerate(50)
    tesla.get_info()
