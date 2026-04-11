#include <iostream>
#include <string>
using namespace std;

int main() {
    string nombre;
    float nota1, nota2, nota3, promedio;

    // Solicitar nombre del estudiante (permite espacios)
    cout << "========================================" << endl;
    cout << "   SISTEMA DE CALCULO DE PROMEDIO" << endl;
    cout << "========================================" << endl;
    cout << "Ingrese el nombre del estudiante: ";
    getline(cin, nombre);

    // Ingresar y validar nota 1
    do {
        cout << "Ingrese la nota 1 (0 - 100): ";
        cin >> nota1;
        if (nota1 < 0 || nota1 > 100)
            cout << "  [!] Nota invalida. Debe estar entre 0 y 100." << endl;
    } while (nota1 < 0 || nota1 > 100);

    // Ingresar y validar nota 2
    do {
        cout << "Ingrese la nota 2 (0 - 100): ";
        cin >> nota2;
        if (nota2 < 0 || nota2 > 100)
            cout << "  [!] Nota invalida. Debe estar entre 0 y 100." << endl;
    } while (nota2 < 0 || nota2 > 100);

    // Ingresar y validar nota 3
    do {
        cout << "Ingrese la nota 3 (0 - 100): ";
        cin >> nota3;
        if (nota3 < 0 || nota3 > 100)
            cout << "  [!] Nota invalida. Debe estar entre 0 y 100." << endl;
    } while (nota3 < 0 || nota3 > 100);

    // Calcular promedio
    promedio = (nota1 + nota2 + nota3) / 3;

    // Mostrar resultados
    cout << endl;
    cout << "========================================" << endl;
    cout << "   RESULTADO" << endl;
    cout << "========================================" << endl;
    cout << "Estudiante : " << nombre << endl;
    cout << "Nota 1     : " << nota1 << endl;
    cout << "Nota 2     : " << nota2 << endl;
    cout << "Nota 3     : " << nota3 << endl;
    cout << "Promedio   : " << promedio << endl;
    cout << "----------------------------------------" << endl;

    // Evaluar resultado
    if (promedio > 90) {
        cout << "Estado     : APROBADO con EXCELENCIA" << endl;
    } else if (promedio >= 71) {
        cout << "Estado     : APROBADO" << endl;
    } else {
        cout << "Estado     : REPROBADO" << endl;
    }

    cout << "========================================" << endl;

    return 0;
}