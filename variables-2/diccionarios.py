diccionario_ejemplo = dict(nombre='Juan', edad=30, ciudad='Madrid')
diccionario_correcto = {
  'nombre': 'Juan',
  'edad': 30,
  'ciudad': 'Madrid'
}
diccionario_correcto['nombre'] = 'Maria'
print('----------------------')
print(f'diccionario_ejemplo: {diccionario_ejemplo}')
print(f'diccionario_correcto: {diccionario_correcto}')
print('----------------------')

for clave in diccionario_ejemplo.keys():
  print(f'Clave: {clave}, Valor: {diccionario_ejemplo[clave]}')
  print('----------------------')

for value in diccionario_correcto.values():
  print(f'Valor: {value}')
  print('----------------------')

for clave, valor in diccionario_correcto.items():
  print(f'Clave: {clave}, Valor: {valor}')
  print('----------------------')


# Para trabajar con indices en el for in, se debe trabajar con la funcion enumerate()
for indice, (clave, valor) in enumerate(diccionario_ejemplo.items()):
  print(f'El indice {indice} que seria el elemento {indice + 1}, corresponde a la clave {clave} y valor {valor}')
  print('----------------------')

# Si necesito iniciar el valor del indice en 1, puedo usar el "start=1" como segundo parametro de enumerate()
for indice, (clave, valor) in enumerate(diccionario_ejemplo.items(), start=1):
  print(f'El Elemento {indice} corresponde a la clave {clave} y valor {valor}')
  print('----------------------')

# FROMKEYS() crear un diccionario solamente con los keys (sin valores)
diccionario_con_keys = dict.fromkeys(['nombre', 'edad', 'ciudad'], 'Desconocido')# Si no se le pasa el segundo parametro 'Desconocido', el valor para cada key sera None
print(f'diccionario_con_keys: {diccionario_con_keys}')