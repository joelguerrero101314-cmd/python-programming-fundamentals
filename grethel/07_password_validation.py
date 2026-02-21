def main():

    # Inicio
    username = input("Ingrese su usuario: ")
    print("Hola", username)

    # Contraseña
    password = "itse1234"

    # Validación
    validation = input("Ingrese la contraseña: ")

    # Casos
    if validation == password:
        print("Acceso autorizado")

    else:
        print("Contraseña incorrecta. Intente nuevamente")


main()
