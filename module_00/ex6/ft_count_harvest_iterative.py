def ft_count_harvest_iterative() -> None:
    day_until_harvest: int = int(input("Days until harvest: "))
    for x in range(day_until_harvest):
        print("Day", x)
    print("Harvest time!")
