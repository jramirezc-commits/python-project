nueva_lista = ['Hola', 'Mundo']

# Agregar elementos
nueva_lista.append('!')
nueva_lista.insert(0, 'Saludos:')
nueva_lista.insert(2, 'Jairo')
nueva_lista.extend(['¿Cómo', 'estás?'])

# Eliminar elementos
nueva_lista.remove('Mundo')
nueva_lista.pop(0)

# Elimina todos los datos de la lista
# nueva_lista.clear()

# Acceder a elementos
primer_elemento = nueva_lista[0]
ultimo_elemento = nueva_lista[-1]

# Imprimir resultados
# print(nueva_lista)
# print(primer_elemento)
# print(ultimo_elemento)

lista_numerica = [1, 2, 3, 4, 5]

# Ordena de menor a mayor
lista_numerica.sort()
# Ordena de mayor a menor
lista_numerica.reverse()

print(lista_numerica)

# Encontrar el indice de un valor dado
print(lista_numerica.index(3))