# def main():
#     number = float(input("Ingresa un número: "))

#     if number > 0:
#         print("El número es POSITIVO ")
#     elif number < 0:
#         print("El número es NEGATIVO ")
#     else:
#         print("El número es CERO ")

# main()

def verificar_signo_numero():
    number_entry: float = float(input("Ingresa un número: "))

    if number_entry > 0:
        print("El número es POSITIVO")
    elif number_entry< 0:
        print("El número es NEGATIVO")
    else:
        print("El número es CERO")
        
verificar_signo_numero()
