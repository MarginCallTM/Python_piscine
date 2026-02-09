class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")

    def set_height(self, height):
        if height < 0:
            print(
                f"\nInvalid opreation: height {height}cm [REJECTED]")
            print("Security : Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(
                f"Invalid operation attempted: age {age} days [REJECTED]\n")
            print("Security : Negative height rejected\n")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def display_info(self):
        print(
            f"\nCurrent plant:{self.name}({self._height}cm,{self._age} days)")


def main():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)

    plant.display_info()


if __name__ == "__main__":
    main()
