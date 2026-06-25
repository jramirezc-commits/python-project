conjuntos = {'Primer-Elemento', 'Segundo-Elemento'}

# Con la funcion enumerate(), puedo obtener un indice
for indice, elemento_conjunto in enumerate(conjuntos, start=1):
  print(f'Elemento {indice} del conjunto: {elemento_conjunto}')

print('----------------------')

diccionario = {
  'nombre': 'Juan',
  'edad': 30,
  'ciudad': 'Madrid'
}

for indice, (clave, valor) in enumerate(diccionario.items(), start=1):
  print(f'Elemento {indice} del diccionario: Clave={clave}, Valor={valor}')

print('----------------------')

# Iterar dos Elementos al mismo tiempo con zip()
animales = ['Perro', 'Gato', 'Conejo']
edades = [5, 3, 2]

for animal, edad in zip(animales, edades):
  print(f'El {animal} tiene {edad} años.')

print('----------------------')

# Con la funcion zip() se puede iterar varios elementos al mismo tiempo
for elemento_conjunto, (clave, valor) in zip(conjuntos, diccionario.items()):
  print(f'Elemento del conjunto: {elemento_conjunto}, Elemento del diccionario: Clave={clave}, Valor={valor}')

print('----------------------')

for indice, (elemento_conjunto, (clave, valor)) in enumerate(zip(conjuntos, diccionario.items())):
  print(f'Elemento {indice} del conjunto: {elemento_conjunto}, Elemento del diccionario: Clave={clave}, Valor={valor}')

print('----------------------')


# for/else
for elemento_conjunto, (clave, valor) in zip(conjuntos, diccionario.items()):
  print(f'Elemento del conjunto: {elemento_conjunto}, Elemento del diccionario: Clave={clave}, Valor={valor}')
  break
else:
  print('Se han iterado todos los elementos sin interrupciones.')

print('----------------------')


# Multiplicar por 2 cada elemento de la lista de numeros
numeros_lista = [1, 2, 3, 4, 5]
for numero in numeros_lista:
  print(f'Elemento de la lista: {numero * 2}')

resultado_multiplicacion = [numero * 2 for numero in numeros_lista] # List comprehension
print(f'Resultado de la multiplicación: {resultado_multiplicacion}')