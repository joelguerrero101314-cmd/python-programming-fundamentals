def main():
    print("multipliquemos juntos")
    
    number = int(input("Escoja el numero que desea multiplicar: "))
    
    for i in range (1, 11):
        Result = number * i
        print (f"{number} x {i} ={Result}")
main() 