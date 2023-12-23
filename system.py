import random

poweron_option = "\n1. Select \"1\" to boot \n2. Select \"2\" to exit"
poweroff_option = "\n1. Select \"1\" to Shutdown \n2. Select \"2\" to Reboot"
unlock_option = "\n1. Select \"1\" to unlock \n2. Select \"2\" for power options"
lock_option = "\n1. Select \"1\" to lock \n2. Select \"2\" for power options "
home_option = "\n1. Select \"1\" for home menu \n1. Select \"2\" to show lock options "
homeMenu_option = "\n1. Select \"1\" for make BUGDET \n2. Select \"2\" to play ROCK, PAPER, SCISSORS "

def powerOn():
	while True:
		print(poweron_option)
		powerOn_input = input("Select an option: ")
		if powerOn_input == "1":
			print("Booting please wait.....\n")
			print("Power on!")
			unLock()
			break
		elif powerOn_input == "2":
			print("Exiting please.....")
			break

def powerOff():
	while True:
		print(poweroff_option)
		powerOff_input = input("Select an option: ")
		if powerOff_input == "1":
			print("Shutting down please wait....")
			print("Power off")
			powerOn()
			break
		elif powerOff_input == "2":
			print("Reboot booting please wait....\n")
			print("Power on!!")
			unLock()
			break

def unLock():
	while True:
		print(unlock_option)
		unLock_input = input("Select an option: ")
		if unLock_input == "1":
			print("Please wait.....")
			print("\nUnlocked!")
			Home()
			break
		elif unLock_input == "2":
			print("\nShowing power options")
			powerOff()
			break

def Lock():
	while True:
		print(lock_option)
		lock_input =  input("Select an option: ")
		if lock_input == "1":
			print("Please wait.....")
			print("\nLocked!")
			unLock()
			break
		elif lock_input == "2":
			print("Showing power options")
			powerOff()
			break

def Home():
	while True:
		print(home_option)
		homeOption_input = input("Select an option: ")
		if homeOption_input == "1":
			print("Please wait....")
			print("\nShowing Home!!")
			homeMenu()

			
		elif homeOption_input == "2":
			print("Please wait...")
			print("\nShowing lock options")
			Lock()
			break

def rps():

    choices = "\n1. Rock⛰️ \n2. Paper📜 \n3. Scissors✂️ \n4. Show scores📊🔢 \n5. EXIT👋🚶"


    players_score = 0
    computer_score = 0

    while True:
        print(choices)
        players_choice = int(input("Select a choice: "))

        if players_choice == 5:
            print("Thanks for playing")
            break


        elif players_choice == 4:
            print("Your Score👦:", players_score, "Computer Score🖳:", computer_score)
        elif players_choice in [1, 2, 3]:
            computer_choice = random.randrange(1, 4)

            if players_choice == computer_choice:
                print("DRAW", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
            elif players_choice == 1 and computer_choice == 2:
                computer_score += 1
                print("COMPUTER WINS ⛰ X 📜", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
            elif players_choice == 1 and computer_choice == 3:
                players_score += 1
                print("YOU WIN ⛰ X ✂", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
            elif players_choice == 2 and computer_choice == 1:
                players_score += 1
                print("YOU WIN 📜 X ⛰", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
            elif players_choice == 2 and computer_choice == 3:
                computer_score += 1
                print("COMPUTER WINS 📜 X ✂", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
            elif players_choice == 3 and computer_choice == 1:
                computer_score += 1
                print("COMPUTER WINS ✂ X ⛰", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------",)
            elif players_choice == 3 and computer_choice == 2:
                players_score += 1
                print("YOU WIN ✂ X 📜", "\n-------------\nYour Score👦:", players_score, "\nComputer Score🖳:", computer_score,"\n-------------")
        else:
            print("Select a valid option⚠️")


def budget():
	options_choice = "\n1. Select 1 to add an item \n2. Select 2 to remove an item \n3. Select 3 to show budget items \n4. Select 4 to clear budget \n5. Select \"5\" to exit"
	goods = []



	def myOption():
		while True:
			print(options_choice)
			option = input("\nSelect an option: ")
			if option == "1":
				budget = input("enter an item: ")	
				goods.append(budget)
			elif option == "2":
				remove = input("remove an item: ")
				if remove not in goods:
					print("Item not found")
					myOption()
				print("removing item.....")
				goods.remove(remove)
				print("item removed")
			elif option == "3":
				print("Showing your budget")
				for budgetItems in goods:
					print(budgetItems)
				print("budget item is", len(goods))
			elif option == "4":
				print("Deleting budget....")
				goods.clear()
			elif option == "5":
				print("Exiting please wait......")
				break

	myOption()

def homeMenu():
	print(homeMenu_option)
	homeMenu = input("Select an option: ")
	if homeMenu == "1":
		print("Opening budget.....")
		budget()

	elif homeMenu == "2":
		print("Opening ROCK, PAPER, SCISSORS")
		rps()



powerOn()
