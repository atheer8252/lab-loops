while True:
    user_input = input("Please enter a number: ")

    # Check if the input is a number
    if user_input.isdigit():
        number = int(user_input)
        print("Valid input:", number)
        break  # Exit the loop if the input is valid
    else:
        print("Invalid input, please try again.")