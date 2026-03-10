import sys


class InventoryMaster:

    def __init__(self) -> None:
        pass

    def parse_args(self, argv) -> dict:
        inventory = {}
        for arg in argv[1:]:
            parts = arg.split(":")
            if len(parts) != 2:
                print(f"Error: '{arg}' is not valid.")
                print("Usage: item: Quantity (ex: sword:1 Or potion:5)")
                return None
            try:
                name = parts[0]
                quantity = int(parts[1])
                if name in inventory:
                    print(
                        f"Error: '{name}' is mentionned twice")
                    return None
                inventory[name] = quantity
            except ValueError:
                print(f"Error: '{parts[1]}' is not a valid quantity.")
                print("Usage: quantity must be a number (ex: sword:1)")
                return None
        return inventory

    def count_item_len(self, inventory) -> int:
        return len(inventory)

    def count_item_quantity(self, inventory) -> int:
        total = 0
        for quantity in inventory.values():
            total += quantity
        return total

    def display_inventory_overview(self, inventory) -> None:
        total = self.count_item_quantity(inventory)
        types = self.count_item_len(inventory)

        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {types}")

    def display_detail_inventory(self, inventory) -> None:
        print("\n=== Current Inventory ===")
        if not inventory:
            print("Inventory is empty!")
            return
        total = self.count_item_quantity(inventory)
        sorted_inventory = sorted(
            inventory.items(),
            key=lambda x: x[1],
            reverse=True)

        for name, quantity in sorted_inventory:
            percentage = round((quantity / total) * 100, 1)
            unit = "unit" if quantity == 1 else "units"
            print(f"{name}: {quantity} {unit} ({percentage}%)")

    def inventory_statistics(self, inventory) -> None:
        print("\n=== Inventory Statistics ===")
        if not inventory:
            print("Inventory is empty!")
            return
        most_abundant = max(inventory.items(), key=lambda x: x[1])
        least_abdundant = min(inventory.items(), key=lambda x: x[1])

        most_unit = "unit" if most_abundant[1] == 1 else "units"
        least_unit = "unit" if least_abdundant[1] == 1 else "units"

        print(
            f"Most abundant: {most_abundant[0]}"
            f" ({most_abundant[1]} {most_unit})")
        print(
            f"Least abundant: {least_abdundant[0]}"
            f" ({least_abdundant[1]} {least_unit})")

    def categorize_inventory(self, inventory) -> None:
        print("\n=== Item Categories ===")
        if not inventory:
            print("Inventory is empty!")
            return
        categories = {
            "Abundant": {},
            "Moderate": {},
            "Scarce": {}
        }
        for name, quantity in inventory.items():
            if quantity >= 10:
                categories["Abundant"][name] = quantity
            elif quantity >= 4:
                categories["Moderate"][name] = quantity
            else:
                categories["Scarce"][name] = quantity

        for category, items in categories.items():
            if items:
                print(f"{category}: {items}")

    def management_suggestions(self, inventory) -> None:
        print("\n=== Management Suggestion ===")
        if not inventory:
            print("Inventory is empty!")
            return
        scarce_items = []
        for name, quantity in inventory.items():
            if quantity < 4:
                scarce_items.append(name)
        if scarce_items:
            print(f"Restock needed: {', '.join(scarce_items)}")

    def dictionary_properties_demo(self, inventory) -> None:
        print("\n=== Dictionary Properties Demo ===")
        keys = ', '.join(inventory.keys())
        values = ', '.join(str(v) for v in inventory.values())
        print(f"Dictionary keys: {keys}")
        print(f"Dictionary values: {values}")
        search = input("Search an item in the inventory: ")
        result = search in inventory
        print(f"Sample lookup - '{search}' in inventory: {result}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    items = InventoryMaster()

    inventory = items.parse_args(sys.argv)

    if inventory is None:
        sys.exit(1)
    if not inventory:
        print("Usage: item:quantity (ex: sword:1)")
        sys.exit(1)
    items.display_inventory_overview(inventory)

    items.display_detail_inventory(inventory)

    items.inventory_statistics(inventory)

    items.categorize_inventory(inventory)

    items.management_suggestions(inventory)

    items.dictionary_properties_demo(inventory)
