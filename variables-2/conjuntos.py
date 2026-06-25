# Una forma de asignar conjuntos
conjunto = set(['Primer-Elemento', 'Segundo-Elemento']) # Esta forma no se recomienda por python
conjunto_final = {'Primer-Elemento', 'Segundo-Elemento'}
print('-----------------')
print(conjunto)
print('-----------------')


conjunto_vacio = set()
conjunto_vacio.add('Dato 1')
conjunto_vacio.add('Dato 1')# add agrega de a un dato a los conjuntos
conjunto_vacio.update(['Dato 2', 'Dato 3'])# update sirve para agregar varios datos
print(f'conjunto_vacio: {conjunto_vacio}')
print('-----------------')

# Si quiero obtener un solo elemento del conjunto (por medio del indice por ejemplo)
type_changed = list(conjunto_vacio) # Se debe convertir a lista primero
print(f'Primer elemento del conjunto: {type_changed[0]}')
print('-----------------')

# insertando un conjunto dentro de otro conjunto con ayuda de frozenset()
preparar_conjunto = frozenset(conjunto_vacio)
conjunto_anidado = {'conjunto', 'anidado', preparar_conjunto}
print(f'conjunto_anidado: {conjunto_anidado}')
lista_anidada = list(conjunto_anidado)
print(f'lista_anidada: {lista_anidada}')
print('-----------------')

# Encontrar elementos en comun de dos conjuntos
mis_amigos = {'Ana', 'Luis', 'Pedro', 'María'}
amigos_de_pedro = {'Luis', 'Carlos', 'María', 'Sofia'}
en_comun = mis_amigos & amigos_de_pedro # → {'Luis', 'María'}
print(f'Datos en comun: {en_comun}')
print('-----------------')

# Encontrar diferencias entre dos conjuntos
inscritos = {'Ana', 'Luis', 'Pedro', 'María'}
asistieron = {'Ana', 'Pedro'}
faltaron = inscritos - asistieron # → {'Luis', 'María'}
print(f'Datos que faltaron: {faltaron}')
print('-----------------')

# Validar que no hayan duplicados
codigos = ['A01', 'B02', 'C03', 'A01']
cantidad_elementos_lista = len(codigos)# Se cuenta la cantidad de elementos en la lista
cantidad_elementos_sin_duplicados = len(set(codigos)) # Se convierte lista a conjunto para elliminar duplicados y se cuenta la cantidad de elementos que quedaron
if cantidad_elementos_lista != cantidad_elementos_sin_duplicados:
  print('Hay codigos duplicados, valida detenidamente')
  print('-----------------')


# TEORIA DE CONJUNTOS EN PYTHON
conjunto_primero = {1, 2, 3, 4, 6}
conjunto_segundo = {8, 9, 5}
is_conjunto = conjunto_segundo.issubset(conjunto_primero)# conjunto_segundo es un subconjunto de conjunto_primero?
print(is_conjunto)
print(conjunto_segundo < conjunto_primero)# Es otra forma de preguntar lo anterior
#NOTA: Para que las validaciones anteriores sean True, ambos deben tener 100% de coincidencia
print('-----------------')
is_some_similar = conjunto_segundo.isdisjoint(conjunto_primero)# conjunto_segundo no tiene elementos en comun con conjunto_primero?
print(is_some_similar)
print('-----------------')