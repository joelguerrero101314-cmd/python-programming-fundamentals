def password_validation() -> None:
    correct_password: str = "N3twork1"

    user_password: str = ""

    while user_password != correct_password:

        user_password = input("Ingresa la contraseña: ") 

        if user_password != correct_password:

            print("Contraseña incorrecta, intenta de nuevo")


    print("Contraseña correcta")
    

password_validation()