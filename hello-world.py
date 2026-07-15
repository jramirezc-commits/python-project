# Introduccion a Python
nombre = "pepito"
print(f"¡Hola, {nombre}!")

tupla = ('Hola', 'Mundo')
tupla = 'Hola', 'Mundo'
print(tupla[0])  # Imprime 'Hola' en la consola

lista = [0, 1, 2, 3, 2, 1, 5, 4]
final_data = set(lista)
print(final_data)

conjunto = {'Primero', 'Segundo', 'Tercero', 'Segundo'}
conjunto2 = set(['Cuarto', 'Quinto'])
print(f'conjunto {conjunto}')
print(f'conjunto 2: {conjunto2}')
another_data = set(conjunto)
print(f'another data: {another_data}')

# Para acceder a un item en especifico de un conjunto, se debe validar que existe el dato y convertiri a lista
if 'Segundo' in conjunto:
    lista_conjunto = list(conjunto)
    print(f'Elemento "Segundo" encontrado en el conjunto: {lista_conjunto[1]}')

result = f'Elemento "Segundo" encontrado en el conjunto {list(conjunto)[1]}' if 'Segundo' in conjunto else 'Elemento no encontrado'#Usando el operador ternario de if/else
print(f'RESULTADO: {result}')

# Diccionarios (en javascript seria como los json)
diccionario = {
    'nombre': 'pepito',
    'edad': 5,
    'juguetes': ['pelota', 'muñeca']
}
print(f"Nombre: {diccionario['nombre']}")

# Otra forma de obtener un valor en especifico de un diccionario
age_value = diccionario.get('edad')
print(f"Edad: {age_value}")

# En python existe una forma de trabajar con un objeto como en javascript de la siguiente manera:
from types import SimpleNamespace # Importando esta libreria que viene con python desde la version 3.3

persona = SimpleNamespace(
    nombre="Jairo",
    edad=25
)
persona.nombre  # "Jairo"

# /////////////////////
# PRINT()
# ///////////////////////

print('Resultado', result, sep=': ', file=open('expresiones_regulares//resultados.txt', 'a'), end='.\n')
# sep= — Separador entre valores
# file= — Imprimir a un archivo en vez de consola
# end= — Qué poner al final
# flush= — Forzar la impresión inmediata (False por defecto)