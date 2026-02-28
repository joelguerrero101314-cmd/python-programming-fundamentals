def main():
  
  # Bienvenida
  print("Menú de Operaciones Matemáticas")
  
  # Bucle
  option = 0
  while option != 4:
    
    # Menú
    print("1. Sumar\n 2. Restar\n 3. Multiplicar\n 4. Salir")
    option = int(input("Selecciona una opción: "))
    
    number1 = int(input("Ingresa el primer número: "))
    number2 = int(input("Ingresa el segundo número: "))
    
    match option:
      
      case 1:
        sum_numbers = number1 + number2
        print(f"La suma es {sum_numbers}")
      
      case 4:
        print("Programa terminado.")



main() 