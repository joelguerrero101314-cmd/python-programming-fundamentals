def main():
  
  # Bienvenida
  print("Menú de Operaciones Matemáticas")

  
  #Bucle
  option = 0
  while option != 4:
    
    # Menu
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Salir")
    option = int(input("Escoge una opción: "))

    # Casos
    match option:
      
        case 1:
          number1 = int(input("Ingresa el primer número: "))
          number2 = int(input("Ingresa el segundo número: "))
          sum_numbers = number1 + number2
          print(f"La suma es {sum_numbers}")
          
        case 2:
          number1 = int(input("Ingresa el primer número: "))
          number2 = int(input("Ingresa el segundo número: "))
          substract_numbers = number1 - number2
          print(f"La resta es {substract_numbers}")
        
        case 3:
          number1 = int(input("Ingresa el primer número: "))
          number2 = int(input("Ingresa el segundo número: "))
          multiply_numbers = number1 * number2
          print(f"La multiplicación es {multiply_numbers}")
      
        case 4:
          print("Programa terminado.")

main() 