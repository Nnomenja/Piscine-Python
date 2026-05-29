def ft_count_harvest_recursive() -> None:
    def iterative_helper(value: int, max: int) -> None:
        print("Day", value)
        if (value == max):
            return
        else:
            iterative_helper(value + 1, max)
    day_until_harvest: int = int(input("Days until harvest: "))
    iterative_helper(1, day_until_harvest)
    print("Harvest time!")
