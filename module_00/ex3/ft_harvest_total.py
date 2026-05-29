def ft_harvest_total() -> None:
    sum: int = 0
    for x in range(3):
        label: str = "Day " + str(x + 1) + " harvest: "
        sum += int(input(label))
    print("Total harvest: ", sum)
