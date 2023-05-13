# Define the menu options
menu = {
    "1": "Addition",
    "2": "Subtraction",
    "3": "Multiplication",
    "4": "Division",
    "Q": "Exit"
}

# Print the welcome message
print("Welcome to the Calculator App!\n")

# Print the menu options
for option in menu:
    print(f"{option}. {menu[option]}")

# Loop until the user chooses to exit
while True:
    # Ask the user for their choice
    choice = input("\nEnter your choice: ")

    # Check if the user wants to exit
    if choice.upper() == "Q":
        print("\nThank you for using the Calculator App!")
        break

    # Check if the choice is valid
    if choice not in menu:
        print("\nInvalid choice, please try again.")
        continue

    # Ask the user for their numbers
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    # Perform the calculation based on the user's choice
    if choice == "1":
        result = num1 + num2
        operation = "+"
    elif choice == "2":
        result = num1 - num2
        operation = "-"
    elif choice == "3":
        result = num1 * num2
        operation = "*"
    elif choice == "4":
        result = num1 / num2
        operation = "/"
    else:
        result = None

    # Print the result
    if result is not None:
        print(f"\n{num1} {operation} {num2} = {result}\n")
