def main():

    # Inicio
    username = input("Ingrese su usuario: ")
    print("Hola", username)

    # Contraseña correcta
    password = "itse1234"
    validation = ""

    # Validación
    while validation != password:
        validation = input("Ingrese la contraseña: ")

        if validation == password:
            print("Acceso autorizado")
        else:
            print("Contraseña incorrecta. Intente nuevamente")


main()
