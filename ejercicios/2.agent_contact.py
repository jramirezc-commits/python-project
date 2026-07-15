diccionario = {
  'Juan': '312098',
  'Sofia': '123456',
  'Claudia': '321456'
}

def add_contact(name, phone):
  if name and phone:
      diccionario[name]= phone


name = input('Ingresa un nuevo contacto: ')
phone_number = input(f'Ahora ingresa el numero de {name}: ')

if name != '' and phone_number != '':
  add_contact(name, phone_number)
else:
  print('No se detecto un nuevo contacto.')

print(diccionario.keys())