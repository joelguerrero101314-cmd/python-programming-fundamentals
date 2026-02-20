def start_countdown ()-> None: 

    number: int = int (input( "Agrega el numero donde deseas empezar la cuenta regresiva: " ))

    while number >= 0:

        print(number)

        number -= 1

start_countdown()