def main():
    #Título
    print("Contador Regresivo")
    number = int(input("Ingresa un número del 1 al 50: "))
    
    if 0 < number <= 50:
        for i in range(number, -1, -1):
            print(i)
    
    else:
        print("Ingresa un número dentro del rango.")
    
    
main()