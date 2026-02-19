def main():
   #Bienvenido
   print("Bienvenido a la Calculadora de Tablas de Multiplicar") 
   number = int(input("Ingresa el número que quieres multiplicar: "))
   
   #Operación
   for i in range(1,11):
       multiplication = i * number
       
       print(i, "*", number, "=",multiplication)
    
    
main()