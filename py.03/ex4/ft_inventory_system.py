import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            key, value = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    amount_total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {amount_total}")
    for item in inventory:
        percentage = round(inventory[item] / amount_total * 100, 1)
        print(f"Item {item} represents {percentage}%")
    print(f"Item most abundant: ")
    inventory.update("magic_item" : 1
    print(f"Updated inventory: 


if __name__ == "__main__":
    main()
