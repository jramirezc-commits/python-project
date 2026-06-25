from create_password import crear_password_random

password, valor_original = crear_password_random(12)
print(f'La nueva contraseña generada a partir del valor {valor_original} es: {password}')

exit()

#args permite que una función reciba cualquier cantidad de argumentos posicionales, sin definir cuántos serán de antemano.
# Utilizando el parametro args
def crear_password_random_args(*args):
    passwords = []
    for num in args:
        password, _ = crear_password_random(num)
        passwords.append(password)
    return passwords

password = crear_password_random_args(12, 22, 32)
print(f'Las nuevas contraseñas generadas son: {password}')

# Funcion suma con args
def sumar(*numero):
  resultado = sum(numero)
  return resultado

valores_sumados = sumar(2, 5, 3, 10)
print(f'Los valores sumados son: {valores_sumados}')


print('--------FUNCIONES LAMBDA-----------')
# CREANDO FUNCIONES CON LAMBDA
multiplicar_numero = lambda numero: numero * 2
print(multiplicar_numero(5))

#Saber si un numero es par o impar
es_par = lambda numero: "Par" if numero % 2 == 0 else "Impar" # Se usa el operador ternario de if/else
print(es_par(5))

#Haciendo lo mismo que el anterior ejercicio pero con filter()
numeros = [1, 10, 5, 3, 8]
# is_par = list(filter(lambda numero: numero % 2 == 0, numeros))
# print(f'Es par?: {is_par}')
is_par = [numero for numero in numeros if numero % 2 == 0]# Usando list comprehension
print(f'Es par?: {is_par}')

#funcion map()
# is_par_map = list(map(lambda numero: 'Par' if numero % 2 == 0 else 'Impar', numeros))
is_par_map = ['Par' if numero % 2 == 0 else 'Impar' for numero in numeros] # Usando list comprehension
print(f'Es par (map)?: {is_par_map}')

#funcion map()
nombres = ['jairo', 'pedro', 'ana']
edades = [25, 30, 22]

def show_profile(name, age):
  return f'Nombre: {name}: {age} años'

# resultado_iteracion = [show_profile(name, age) for name, age in zip(nombres, edades)]# Usando list comprehension para iterar con zip() y mostrar el perfil de cada persona
resultado_iteracion = list(map(show_profile, nombres, edades))
print(f'Perfiles: {resultado_iteracion}')


def show_age(item):
  print(f'Edad: {item[1]}')
  return item[1]

print('----------------Ejercicio-------------------')
compañeros = [('Juan', 31), ('Martha', 30)]
compañero = ('Jairo', 34)
compañeros.append(compañero)
print(compañeros)
compañeros.sort(key= lambda item: item[1])#sort es para ordenar, en este caso ordena por edad que es el segundo item
compañeros.sort(key= show_age)
print(f'compañeros ordenados por edad: {compañeros}')