califications = [4.5, 7.0, 3.2, 9.0, 5.5, 2.0]
aprobados = []

for nota in califications:
    if nota >= 5:
      aprobados.append(nota)

if len(aprobados) > 0:
  aprobados.sort()

print(f'Lista de los aprobados: {aprobados}')