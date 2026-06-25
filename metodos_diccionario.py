diccionario = {
    'nombre': 'Jairo',
    'edad': 25,
    'ciudad': 'Madrid'
}

count_dictionary = len(diccionario)
account_dictionary = diccionario.__len__()
# print(count_dictionary)
# print(account_dictionary)


result = diccionario.pop('edad', 'El valor ya fue eliminado') # Elimina la clave 'edad', si no la encuentra, muestra el mensaje 'El valor ya fue eliminado'
print(result)
print(diccionario)