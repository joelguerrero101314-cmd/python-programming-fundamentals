def main():
  
  #Bienvenida
  print("Calculadora de Promedio de Notas")
  
  #Notas
  grade_1 = int(input("Ingresa la primera nota: "))
  grade_2 = int(input("Ingresa la segunda nota: "))
  grade_3 = int(input("Ingresa la tercera nota: "))
  grade_4 = int(input("Ingresa la cuarta nota: "))
  grade_5 = int(input("Ingresa la quinta nota: "))
  
  #Operacion
  sum_grades = grade_1 + grade_2 + grade_3 + grade_4 + grade_5
  average = sum_grades/5
  
  #Condición
  if average >= 70:
    print("Aprobaste la materia.") 
    print(average)
    
  else:
    print("Reprobaste la materia.")
    print(average)
  
main()