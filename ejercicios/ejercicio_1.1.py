# Datos de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

# A. Encontrar la diferencia en porcentaje entre el curso actual y:
#   - el mas rapido de otros cursos
#   - el mas lento de otros cursos
#   - el promedio de otros cursos

diferencia_contra_min = ((otros_cursos_min - curso_dalto) / otros_cursos_min) * 100
print(f'La efectividad del curso Dalto es del {diferencia_contra_min}% contra el curso mas rapido')

# B. Porcentaje de material insevible que se reduce en:
#   - el promedio de los cursos
#   - el curso actual (este curso)

# C. Ver 10 horas de este curso a cuantas horas de otros cursos equivale? y al reves?
