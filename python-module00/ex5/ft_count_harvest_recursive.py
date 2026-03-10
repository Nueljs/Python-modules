def count_days(harvest, day) -> None:
    if day == harvest:
        print(f"Day {day}")
        return
    else:
        print(f"Day {day}")
        count_days(harvest, day + 1)


def ft_count_harvest_recursive() -> None:
    harvest = int(input("Days until harvest: "))
    count_days(harvest, 1)
    print("Harvest time!")
