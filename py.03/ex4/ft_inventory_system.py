import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            item, quantity = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            inventory[item] = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
    if not inventory:
        print("Empty inventory - usage: "
              "python3 ft_inventory_system.py <item>:<quantity> ...")
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    amount_total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {amount_total}")
    for item in inventory:
        percentage = round(inventory[item] / amount_total * 100, 1)
        print(f"Item {item} represents {percentage}%")
    most_item = ""
    most_quantity = 0
    least_item = ""
    least_quantity = amount_total
    for item in inventory:
        if inventory[item] > most_quantity:
            most_quantity = inventory[item]
            most_item = item
        if inventory[item] < least_quantity:
            least_quantity = inventory[item]
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
