primer_cadena = 'Hola Mundo'
segunda_cadena = 'Adiós Mundo'
tercera_cadena = 'jairo Ramirez'

### DIR = devuelve los atributos que tiene el dato que se le pasa
# print(dir(primer_cadena))
# lo que devuelve:
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Convertir a mayusculas
# print(primer_cadena.upper())
# print(segunda_cadena.upper())

# Convierte a minusculas
# print(primer_cadena.lower())
# print(segunda_cadena.lower())

# Saber la cantidad de caracteres que tiene un string. len es una funcion en python no un metodo.
# print(primer_cadena.__len__())
# print(len(primer_cadena))

# Convierte todo a minusculas y la primer letra a mayuscula
# print (tercera_cadena.capitalize())

# Encuentra una cadena dentro de la cadena que queremos validar, si no encuentra coincidencias, devuelve -1
# print(tercera_cadena.find("Castaño"))

# Nos devuelve el indice de la primera ocurrencia de la subcadena, si no encuentra coincidencias, devuelve un ValueError
# print(tercera_cadena.index("Ramirez"))

# Devuelve la cantidad de coincidencias encontradas en una cadena.
coincidencias = tercera_cadena.count('Ram')
# print(coincidencias)

# Verifica si una cadena comienza con otra cadena
start = primer_cadena.startswith('H')
# print(start)

# Verifica si una cadena termina con otra cadena
end = primer_cadena.endswith('o')
# print(end)

primer_numero = '101'

# El metodo .isnumeric() verifica si un string contiene solo caracteres numéricos. Es un metodo de la clase str
is_number = primer_numero.isnumeric()
# print(is_number)

# Devuelve True solo si la cadena tiene al menos un carácter y todos son letras (sin espacios, números ni símbolos).
is_alpha = primer_numero.isalpha()
# print(is_alpha)
