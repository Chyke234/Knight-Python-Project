# This function prompts the user to enter the knight's name, age, weapon, and armor using the input() function. The age is converted to an integer using the int() function.


def create_knight(knights):
    name = input("Enter the knight's name: ")
    age = int(input("Enter the knight's age: "))
    weapon = input("Enter the knight's weapon: ")
    armor = input("Enter the knight's armor: ")

    knight = {"name": name, "age": age, "weapon": weapon, "armor": armor}

    knights.append(knight)
    print("Knight created successfully!")


all_knights = []

create_knight(all_knights)

# This code defines a function called change_data() that takes a parameter knights, which is expected to be a list of dictionaries representing knights. This function allows the user to modify the attribute of a specific knight based on their input. If the index is out of range (less than 0 or greater/equal to the length of knights), an error message is printed, and the function returns, exiting the function execution.

def change_data(knights):
    knight_index = int(input("Enter the index of the knight you want to modify: "))
    if knight_index < 0 or knight_index >= len(knights):
        print("Invalid knight index!")
        return

    attribute = input(
        "Enter the attribute you want to modify (name, age, weapon, armor): "
    )

    if attribute not in ["name", "age", "weapon", "armor"]:
        print("Invalid attribute!")
        return

    new_value = input(f"Enter the new value for the {attribute}: ")
    knights[knight_index][attribute] = new_value

    print("Knight data modified successfully!")


all_knights = [
    {"name": "Knight 1", "age": 30, "weapon": "Sword", "armor": "Plate"},
    {"name": "Knight 2", "age": 35, "weapon": "Axe", "armor": "Chainmail"},
]

change_data(all_knights)

# Provided code defines a function called select_knight() that takes a parameter knights, which is expected to be a list of dictionaries representing knights. This function allows the user to select and display the details of a specific knight based on their input.

def select_knight(knights):
    knight_index = int(input("Enter the index of the knight you want to select: "))
    if knight_index < 0 or knight_index >= len(knights):
        print("Invalid knight index!")
        return
# The function then prints the details of the selected knight using the print() function. The knight's name, age, weapon, and armor are accessed from the selected_knight dictionary using their respective keys.
    
    selected_knight = knights[knight_index]
    print("Selected Knight:")
    print("Name:", selected_knight["name"])
    print("Age:", selected_knight["age"])
    print("Weapon:", selected_knight["weapon"])
    print("Armor:", selected_knight["armor"])

all_knights = [
    {"name": "Knight 1", "age": 30, "weapon": "Sword", "armor": "Plate"},
    {"name": "Knight 2", "age": 35, "weapon": "Axe", "armor": "Chainmail"},
]

select_knight(all_knights)

# The provided code defines a function called menu() that takes a parameter knights_number, representing the number of knights. This function presents a menu of options related to knights and allows the user to perform various operations on the knights. It utilizes other functions like create_knight(), select_knight(), and change_data() to handle specific tasks.

def menu(knights_number):
    knights = []  # Created an empty list to store the knights

    while True:
        print("\n===== KNIGHT MENU =====")
        print("1. Create a knight")
        print("2. Select a knight")
        print("3. Modify knight data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            create_knight(knights)
        elif choice == "2":
            select_knight(knights)
        elif choice == "3":
            change_data(knights)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")


# Additional functions (create_knight, select_knight, change_data).

knights_count = int(input("Enter the number of knights: "))
menu(knights_count)

knights_number = 0
knights = []


def menu(knights_number):
    knights = []  # Create an empty list to store the knights

    while True:
        print("\n===== KNIGHT MENU =====")
        print("1. Create a knight")
        print("2. Select a knight")
        print("3. Modify knight data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            create_knight(knights)
        elif choice == "2":
            select_knight(knights)
        elif choice == "3":
            change_data(knights)
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")


# Additional functions (create_knight, select_knight, change_data) should be defined separately.

# Example usage
knights_count = int(input("Enter the number of knights: "))
menu(knights_count)

knights_number = 0
knights = []


def create_knight():
    # Logic to create a knight and add it to the 'knights' list
    pass


def select_knight():
    # Logic to select and display information about a knight from the 'knights' list
    pass

# The menu() function is defined. It uses two global variables, knights_number and knights, which are expected to be defined outside the function.The function enters an infinite loop using while True. This allows the menu to be displayed repeatedly until the user chooses to exit.

def menu():
    global knights_number, knights

    while True:
        print("\n===== KNIGHT MENU =====")
        print("1. Create a knight")
        print("2. Select a knight")
        print("3. Modify knight data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_knight()
        elif choice == "2":
            select_knight()
        elif choice == "3":
             change_data()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Call the menu function to start the program
menu()
