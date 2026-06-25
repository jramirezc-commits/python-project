# agregando texto sin eliminar el existente
# with open('archivos//second_file.txt', 'a') as file:
#   file.write('Cuarto texto\n')
#   file.write('Quinto texto\n')


with open('archivos//second_file.txt', 'a') as file:
  for index in range(10):
    file.write(f'Linea {index}\n')
exit()


with open('archivos//second_file.txt', 'a') as file:
  file.writelines([f'Agregando {index}\n' for index in range(10)])
