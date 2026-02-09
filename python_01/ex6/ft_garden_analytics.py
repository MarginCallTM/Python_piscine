class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0

        def record_plant(self, plant):
            self.plants_added += 1

            if isinstance(plant, PrizeFlower):
                self.prize_count += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_count += 1
            else:
                self.regular_count += 1

        def record_growth(self, amount):
            self.total_growth += amount

        def get_report(self):
            return (f"Plants added: {self.plants_added},"
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant typesL: {self.regular_count} regular, "
                    f"{self.flowering_count} flowering,"
                    f"{self.prize_count} prize flowers")


def __init__(self, owner_name):
    self.owner_name = owner_name
    self.plants = []
    self.stats = GardenManager.GardenStats()
    GardenManager.total_gardens += 1


def add_plant(self, plant):
    self.plants.append(plant)
    self.stats.record_plant(plant)
    print(f"Added {plant.name} to {self.owner_name} garden")


def grow_all(self):
    print(f"{self.owner_name} is helping all plants grow...")
    for plant in self.plants:
        plant.grow()
        self.stats.record_growth(1)


def get_garden_score(self):
    return sum(plant.height for plant in self.plants)


def display_report(self):
    print(f"=== {self.owner_name} Garden Report ===")
    print("Plants in garden:")
    for plant in self.plants:
        print(f"- {plant.get_info()}")
    print(self.stats.get_report())


@classmethod
def create_garden_network(cls):
    return f"total gardens managed: {cls.total_gardens}"


@staticmethod
def validate_height(height):
    return height > 0


class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True

    def get_info(self):
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{
            self.name}: {
            self.height}cm , {
            self.flower_color} flowers ({bloom_status})"
class P