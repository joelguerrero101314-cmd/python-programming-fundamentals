def check_age_status() -> None:

    age_input: str = input("Coloca tu edad: ").strip()

    while not age_input.isdigit():
        
        age_input = input("Por favor, introduce un número válido: ").strip()

    age: int = int(age_input)

    if age >= 18:
        print("Eres mayor de edad. ")
    else:
        print("Eres menor de edad.")


check_age_status()