def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} avaible")
    elif unit == "area":
        print(
            f"{seed_type.capitalize()} seeds: covers {quantity} {unit} meters"
        )
    elif unit == "grams":
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
    else:
        print("Unknown unit type")
