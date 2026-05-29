def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit != "packets" and unit != "grams" and unit != "area"):
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: ", end="")
    match unit:
        case "packets":
            print(f"{quantity} packets available")
        case "grams":
            print(f"{quantity} grams total")
        case "area":
            print(f"covers {quantity} square meters")
