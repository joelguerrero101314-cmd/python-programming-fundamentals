def calculate_operation() -> None: 
    
    print("Bienvevido a la Calculadora Simple\n")

    number_1 : int = int(input("Agrega el primer numero: ")) 
    
    number_2 : int = int(input("Agrega el segundo numero: ")) 
    
    operation: str = str(input("Agrega el signo de la operacion que deseas realizar(+ , -, *, /): ")) 

    if operation == "+" :
    
      print("Resultado de la suma seria = ", number_1 + number_2)
    
    elif operation == "-":
    
     print("Resultado de la resta seria = ", number_1 - number_2) 

    elif operation == "*":
      
      print("Resultado de la multiplicacion seria =", number_1 * number_2) 

    elif operation == "/" :
         
        if number_2 != 0:
          
            print ("Resultado de la division seria = ", number_1 / number_2 )

        else :

            print("Error no se puede dividir por 0") 

    else :
     print("Signo invalido, SOLO SE PUEDE UTILIZAR (+, -, *, /)") 

calculate_operation()


