import arithmetic

while True: 
	user_input = raw_input("> ")
	split_input = user_input.split(" ")
	if split_input[0] == "q":
		break
	elif split_input[0] == "+":
		print arithmetic.add(int(split_input[1]), int(split_input[2]))
	elif split_input[0] == "-":
		print arithmetic.subtract(int(split_input[1]), int(split_input[2]))
	elif split_input[0] == "*":
		print arithmetic.multiply(int(split_input[1]), int(split_input[2]))	
	elif split_input[0] == "/":
		print arithmetic.divide(int(split_input[1]), int(split_input[2]))
	elif split_input[0] == "square":
		print arithmetic.square(int(split_input[1]))
	elif split_input[0] == "cube":
		print arithmetic.cube(int(split_input[1]))
	elif split_input[0] == "power":
		print arithmetic.power(int(split_input[1]), int(split_input[2]))
	elif split_input[0] == "mod":
		print arithmetic.mod(int(split_input[1]), int(split_input[2]))