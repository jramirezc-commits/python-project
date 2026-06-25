file = open('archivos//new_file.txt')

# leer archivo completo
# show_all_file = file.read()
# print(show_all_file)
# file.close()

# ////////////////////////
# Otra forma de hacerlo es usando la instrucción with para cerrar el archivo automáticamente al terminar de usarlo.
# with open('archivos//new_file.txt') as file:
#   show_all_file = file.read()
#   print(show_all_file)


# Leer archivo línea por línea, todo queda en una lista[]
# lines = file.readlines()
# print(f'lines >>> {lines}')


# line = file.readline()
# line2 = file.readline()
# print(f'line >>> {line}')
# print(f'line2 >>> {line2}')

# with open('archivos//sample_data.csv', 'r') as file:
#   for line in file:
#     print(line)

with open('archivos//second_file.txt', 'r') as file:
  varias_lineas = file.readlines()
  print(varias_lineas)
  print(varias_lineas[1:])