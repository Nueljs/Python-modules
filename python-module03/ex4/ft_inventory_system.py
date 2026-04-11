import sys


def ft_inventory_system() -> None:
    num_items: int = 0
    inventory: dict = {}
    for arg in sys.argv[1:]:
        item: list = arg.split(":")
        if len(item) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name: str = item[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarting")
            continue
        try:
            value: int = int(item[1])
            inventory[name] = value
            num_items += 1
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {num_items} items:"
          f" {sum(inventory.values())}")
    for item in inventory:
        total_items: int = sum(inventory.values())
        percentage: float = (inventory[item]/total_items) * 100
        print(f"Item {item} represents {percentage:.1f}%")
    items: list = list(inventory.keys())
    first_item: str = list(inventory.keys())[0]
    max_item: str = first_item
    max_val: int = inventory[first_item]
    min_item: str = first_item
    min_val: int = inventory[first_item]
    for name in items:
        current_value: int = inventory[name]
        if current_value < min_val:
            min_item = name
            min_val = current_value
        if current_value > max_val:
            max_item = name
            max_val = current_value
    print(f"Item most abundant: {max_item} with quantity {max_val}")
    print(f"Item least abundant: {min_item} with quantity {min_val}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
