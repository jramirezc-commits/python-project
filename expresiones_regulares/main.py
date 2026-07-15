import re

texto = '''La inteligencia artificial (IA) (de la llamada revolucion 3.00) permite a las máquinas aprender de los datos. linea 1
Hoy en día se usa en asistentes virtuales, autos autónomos y medicina. linea 2
Python es uno de los lenguajes más populares para desarrollar soluciones con IA. linea 3'''

email = 'ejemplo@dominio.com.co'

# result = re.search('inteligencia', texto)
result = re.findall('IA', texto, flags=re.IGNORECASE)
# print('Resultado', result, sep=': ', file=open('expresiones_regulares//resultados.txt', 'a'), end='.\n')

found_digit = re.findall(r'\d', texto)
# print(f'Digitos encontrados: {found_digit}')

found_all_text = re.findall(r'\D', texto)
# print(f'Texto sin digitos: {found_all_text}')

found_all_alphanumeric = re.findall(r'\w', texto)
# print(f'Texto alfanumérico encontrado: {found_all_alphanumeric}')

found_not_alphanumeric = re.findall(r'\W', texto)
# print(f'Texto no alfanumérico encontrado: {found_not_alphanumeric}')

found_empty_places = re.findall(r'\s', texto)
# print(f'Espacios en blanco encontrados: {found_empty_places}')

found_not_empty_places = re.findall(r'\S', texto)
# print(f'Espacios no en blanco encontrados: {found_not_empty_places}')

found_line_breaks = re.findall(r'\n', texto)
# print(f'Saltos de línea encontrados: {found_line_breaks}')

found_all_characters = re.findall(r'.', texto)
# print(f'Todos los caracteres encontrados: {found_all_characters}')

# Con '\' se cancela la busqueda por defecto del . (punto) haciendo que busque un . literal
found_dots = re.findall(r'\.', texto)
# print(f'Simbolos de punto encontrados: {found_dots}')

found_uppercase = re.findall(r'[A-Z]', texto)
# print(f'Mayúsculas encontradas: {found_uppercase}')

found_lowercase = re.findall(r'[a-z]', texto)
# print(f'Minúsculas encontradas: {found_lowercase}')

find_digit_and_enter = re.findall(r'\d\n', texto)
# print(f'Dígitos seguidos de salto de línea encontrados: {find_digit_and_enter}')

find_multiple_digits = re.findall(r'\d{2,3}', texto)
# print(f'Encontrar similitud de minimo 1 digito y maximo 2 digitos: {find_multiple_digits}')

find_start = re.findall(r'^La', texto)
# print(f'Encontrado al inicio del texto: {find_start}')

# print('Encontrado' if re.findall(r'^Hola', texto) else 'No encontrado')

find_start_lines = re.findall(r'^Python', texto, flags=re.MULTILINE)
# print(f'Encontrado al inicio de una línea: {find_start_lines}')

find_final_line= re.findall(r'3$', texto)
# print(f'Encontrado al final de una línea: {find_final_line}')

find_custom = re.findall(r'\d\W\d{2}\)', texto)
# print(f'Encontrado patrón personalizado: {find_custom}')

# con re.sub(), busca que quiere reemplazar, el texto que se va a poner y en que lugar lo quiere reemplazar
# replace = re.sub('dominio', 'dominio_oculto', email)
replace = email.replace('dominio', 'dominio_oculto')
print(f'Email reemplazado: {replace}')





is_email = re.findall(r'[a-zA-Z0-9._]+\@[a-zA-Z0-9.]{2,}.[a-z0-9]{2,10}', email)#El simbolo + permite que haya uno o mas coincidencias antes del @
# print('Email encontrado' if is_email else 'Email no encontrado')
# print(f'Email encontrado: {str(is_email).lower()}')
# is_search = 'dominio' in email

personal_phone_number = '123-456-7890'
encrypt_phone = re.sub(r'\d{3}-\d{3}-\d{4}', '***-***-****', personal_phone_number)
print(f'Teléfono personal encriptado: {encrypt_phone}')