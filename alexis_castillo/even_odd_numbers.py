def even_odd_numbers () -> None: 

    number : int = int(input("Agrega el numero que deseas saber si es par o impar: ")) 

    if number % 2 == 0:
        
        print(f"Numero colocado es par: {number}")

    else:
        
        print(f"Numero colocado es impar: {number}")

even_odd_numbers()