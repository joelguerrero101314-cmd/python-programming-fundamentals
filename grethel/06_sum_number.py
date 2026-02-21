def main():
    
    #Inicio
    print("+ Suma de Números +")
    number = int(input("¡Hola! ¿Hasta qué número quieres sumar?: "))
    
    #Acumulador
    sum = 0
    
    #Operación
    for i in range(1, number + 1):
        sum = sum + i
        
    print(sum)
        
    

main()