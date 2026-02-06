def ft_seed_inventory(seed_type, quantity, unit):
	capitalized_seed = seed_type.capitalize()
	
	if unit == "packets":
		print(f"{capitalized_seed} seeds: {quantity} {unit} available")
	elif unit == "grams":
		print(f"{capitalized_seed} seeds: {quantity} {unit} total")
	elif unit == "area":
		print(f"{capitalized_seed} seeds: covers {quantity} square meters")


	