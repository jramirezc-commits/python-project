with open('archivos//second_file.txt', 'w') as file:
  file.write('Hola mundo\n')
  file.write('Adiós mundo\n')


# Escribir en varias lineas con una sola funcion
with open('archivos//second_file.txt', 'w') as file:
  file.writelines(['Primer texto\n', 'Segundo texto\n', 'Tercer texto\n'])
