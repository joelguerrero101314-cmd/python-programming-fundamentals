def math_menu():
    options : int = 0
    while options != 4:
        print("Math Menu:")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Exit")
        try:
            options = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Please enter a valid integer.")
            options = 0