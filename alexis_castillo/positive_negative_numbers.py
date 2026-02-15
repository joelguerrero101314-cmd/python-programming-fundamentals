def classify_number() -> None:

    user_input: int = int(input("Agrega un numero: ")) 

    if user_input > 0:

        print("The number is positive.")

    elif user_input < 0:

        print("The number is negative.")

    else:
        
        print("The number is zero.")

classify_number()