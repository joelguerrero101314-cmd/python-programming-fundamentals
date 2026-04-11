#include <iostream>
#include <cmath>
using namespace std;

// ---- Funciones de operaciones ----

float sumar(float a, float b) {
    return a + b;
}

float restar(float a, float b) {
    return a - b;
}

float multiplicar(float a, float b) {
    return a * b;
}

float dividir(float a, float b) {
    if (b == 0) {
        cout << "  [!] Error: No se puede dividir entre cero." << endl;
        return 0;
    }
    return a / b;
}

float potencia(float base, float exponente) {
    return pow(base, exponente);
}

// ---- Programa principal ----

int main() {
    int opcion;
    float num1, num2, resultado;
    int contador = 0;

    cout << "========================================" << endl;
    cout << "    MENU DE OPERACIONES MATEMATICAS" << endl;
    cout << "========================================" << endl;

    do {
        // Mostrar menu
        cout << endl;
        cout << "  1. Sumar" << endl;
        cout << "  2. Restar" << endl;
        cout << "  3. Multiplicar" << endl;
        cout << "  4. Dividir" << endl;
        cout << "  5. Potencia (a^b)" << endl;
        cout << "  6. Salir" << endl;
        cout << endl;
        cout << "Seleccione una opcion: ";
        cin >> opcion;

        // Validar opcion
        if (opcion < 1 || opcion > 6) {
            cout << "  [!] Opcion invalida. Intente de nuevo." << endl;
            continue;
        }

        // Ejecutar operacion seleccionada
        if (opcion != 6) {
            cout << "Ingrese el primer numero: ";
            cin >> num1;
            cout << "Ingrese el segundo numero: ";
            cin >> num2;
        }

        switch (opcion) {
            case 1:
                resultado = sumar(num1, num2);
                cout << "Resultado: " << num1 << " + " << num2 << " = " << resultado << endl;
                contador++;
                break;

            case 2:
                resultado = restar(num1, num2);
                cout << "Resultado: " << num1 << " - " << num2 << " = " << resultado << endl;
                contador++;
                break;

            case 3:
                resultado = multiplicar(num1, num2);
                cout << "Resultado: " << num1 << " * " << num2 << " = " << resultado << endl;
                contador++;
                break;

            case 4:
                if (num2 != 0) {
                    resultado = dividir(num1, num2);
                    cout << "Resultado: " << num1 << " / " << num2 << " = " << resultado << endl;
                    contador++;
                }
                break;

            case 5:
                resultado = potencia(num1, num2);
                cout << "Resultado: " << num1 << "^" << num2 << " = " << resultado << endl;
                contador++;
                break;

            case 6:
                cout << endl;
                cout << "========================================" << endl;
                cout << "  Operaciones realizadas: " << contador << endl;
                cout << "  Hasta luego!" << endl;
                cout << "========================================" << endl;
                break;
        }

    } while (opcion != 6);

    return 0;
}