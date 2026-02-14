def main():
    
    #Pregunta al usuario
    number = int(input("¡Hola! Ingresa un número: "))
    
    #Opciones
    if number > 0:
        print("El número es positivo.")
        
    elif number < 0:
        print("El número es negativo.")
        
    elif number == 0:
        print("El número es 0.")
    
main()