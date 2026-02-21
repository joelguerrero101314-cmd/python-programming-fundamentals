def calculate_sum_until_n() -> None:

    number: int = int(input("Agrega un numero: "))

    total_sum: int = 0

    for i in range(1, number + 1):

        total_sum += i

    print("Suma total seria: ", total_sum)


calculate_sum_until_n()
