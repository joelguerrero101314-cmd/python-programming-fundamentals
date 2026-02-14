def main():
    #Bienvenida
    
    print("Bienvenido/a")
    #Pregunta al usuario
    number = int(input("Ingresa un número: "))
    
    #Opciones
    if number > 0:
        print("El número es positivo.")
        
    elif number < 0:
        print("El número es negativo.")
        
    elif number == 0:
        print("El número es 0.")
    
main()