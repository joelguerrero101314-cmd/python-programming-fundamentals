def password_validation() -> None:
    correct_password: str = "12345"

    user_password: str = ""

    while user_password != correct_password:

        user_password = input("Ingresa la contraseña: ")

    print("Contraseña correcta")
    

password_validation()