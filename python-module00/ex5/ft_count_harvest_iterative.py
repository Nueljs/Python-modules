def ft_count_harvest_iterative():
	harvest = int(input("Days until harvest: "))
	days = 0
	while days < harvest:
		days += 1
		print(f"Day {days}")
	if days == harvest : 
		print("Harvest time!")