def main():
    
    #Mensaje de Bienvenida
    print("Bienvenido a la herramienta Calculadora")
    print("=======================================")
    
    #Ingresar números
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))
    
    #Menú
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    option = int(input("¿Cuál operación quieres realizar (1-4)?: "))
        
     #Condiciones
    if option == 1:
        sum_numbers = number1 + number2
        print(number1, "+", number2, "=", sum_numbers)
    
    elif option == 2:
        substract = number1 - number2
        print(number1, "-", number2, "=", substract)
        
    elif option == 3:
        multiply = number1 * number2
        print(number1, "*", number2, "=", multiply)
    
    elif option == 4:
        
        if number2 == 0:
            print("No se puede dividir entre 0.")
            
        else:
            divide = number1 / number2
            print(number1, "/", number2, "=", divide)
            
    else:
        print("Ingresa una opción válida.")

main()