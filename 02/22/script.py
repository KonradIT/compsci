def main():
	print("This is a algorithm that shows two options, and prints the option selected. ")
	print("Pretty useless anyway")
	print("Enter either 1 or 2")
	option=input("Option: ")
	if option == "1":
		print("Option 1 was selected")
		main()
	else:
		if option == "2":
			print("Option 2 was selected")
			exit()
		else:
			print("Please enter 1 or 2")
			main()

if __name__ == "__main__":
    main()
