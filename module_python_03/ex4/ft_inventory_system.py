import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        parts: list[str] = arg.split(":", 1)
        item: str = parts[0]
        raw_val: str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            qty: int = int(raw_val)
            inventory[item] = qty
        except ValueError:
            print(
                f"Quantity error for '{item}': "
                f"invalid literal for int() with base 10: '{raw_val}'"
            )
    return inventory


def print_analytics(inventory: dict[str, int]) -> None:
    print(f"Got inventory: {inventory}")
    items_list: list[str] = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(items_list)} items: {total_qty}")

    if total_qty > 0:
        for item, qty in inventory.items():
            pct: float = (qty / total_qty) * 100
            print(f"Item {item} represents {round(pct, 1)}%")

    most_item: str = max(inventory, key=lambda k: inventory[k])
    least_item: str = min(inventory, key=lambda k: inventory[k])

    print(f"Item most: {most_item} with quantity {inventory[most_item]}")
    print(f"Item least: {least_item} with quantity {inventory[least_item]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    raw_args: list[str] = sys.argv[1:]

    inventory: dict[str, int] = parse_inventory(raw_args)

    if not inventory:
        return

    print_analytics(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
