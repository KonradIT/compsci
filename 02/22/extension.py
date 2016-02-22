def main():
	print("This is a algorithm that shows two options, and prints the option selected. ")
	print("Pretty useless anyway")
	print("Enter either 1, 2 or 3")
	option=input("Option: ")
	if option == "1":
		print("Option 1 was selected")
	else:
		if option == "2":
			print("Option 2 was selected")
			exit()
		else:
			if option == "3":
				calc=input("Type a calculation: ")
				x = eval(calc)
				print(x) 
			else:
				print("Please enter 1, 2 or 3")
				main()

if __name__ == "__main__":
	main()
