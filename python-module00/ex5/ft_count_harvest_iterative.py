def ft_count_harvest_iterative() -> None:
    harvest = int(input("Days until harvest: "))
    days = 0
    for days in range(0, harvest):
        days += 1
        print(f"Day {days}")
    print("Harvest time!")
