def main():
    
    print("numeros positivos y negativos dame algun numero")
    number = int(input("ingrese el numero:"))
    
    if number > 0:
       print("El número es positivo")
    elif number < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero") 
               
main()