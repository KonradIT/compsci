print("PC Part Picker")
print("Menu:\n- start: starts the input of parts\n- show: shows Amazon links for all the parts\n- exit: Exits the program")
pc_setup = []
mobo = ""
gfx = ""
scard = ""
cpu = ""
pwr = ""
case = ""
ram = ""
ramAmount = ""
completed=0
while True:
    selection=input("Enter an option: ")
    if selection == "start":
        mobo=input("Enter the motherboard: ")
        gfx=input("Enter the graphics card: ")
        scard=input("Enter the sound card: ")
        cpu=input("Enter the processor: ")
        pwr=input("Enter the power supply: ")
        ram=input("Enter the RAM stick model: ")
        ramAmount=input("Enter the amount of RAM: ")
        pc_setup.extend([mobo,gfx,scard,cpu,pwr,ram,ramAmount])
        print("Setup saved!")
        completed=1
    if selection == "show":
        if completed == 1:
            print("Motherboard: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[0])
            print("Graphics card: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[1])
            print("Sound card: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[2])
            print("Processor: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[3])
            print("Power supply: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[4])
            print("RAM Stick: http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + pc_setup[5] + pc_setup[6])
        else:
            print("Please run start to fill the part details")
    if selection == "exit":
        exit()
