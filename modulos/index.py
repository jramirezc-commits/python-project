from saludar.saludo import saludando
from sumar_edad.sum_age import sum_age
import sys
sys.path.append('/Users/JRCASTAN/Documents/Cursos/Youtube/Python')
from paquetes import funcion_primera, funcion_segunda

print(f'Hola {saludando("Jairo")}, en 5 años tendras {sum_age(30)}')
print(funcion_primera())
print(funcion_segunda())