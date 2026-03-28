import sys


def ft_inventory_system() -> None:
    inventory: dict = {}
    for arg in sys.argv[1:]:
        item: list = arg.split(":")
        name: str = item[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarting")
        if len(item) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            value: int = int(item[1])
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
        inventory[name] = value
    print(f"Item list: {list(inventory.keys())}")
    for item in inventory:
        total_items: int = sum(inventory.values())
        percentage: float = (inventory[item]/total_items) * 100
        print(f"Item {item} represents {percentage:.1f}%")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
