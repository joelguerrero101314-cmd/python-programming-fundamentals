def generate_multiplication_table()-> None:

    number: int = int(input("Agrega un numero cual quisieras saber la tabla del multiplicar del 1 al 10: ")) 

    for i in range(1, 11): 

        result_multiplication: int = number * i

        print(f" {number} x {i} = {result_multiplication} ")

generate_multiplication_table()