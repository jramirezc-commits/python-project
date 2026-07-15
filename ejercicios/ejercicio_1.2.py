# Suponiendo que cada persona en promedio habla 2 palabras por segundo 
# A. pedirle al usuario que diga cualquier texto real y:
# - Calcular cuanto tardaria en decir esa frase
# - Cuantas palabras dijo?

texto = input('Escribe lo que quieras: ')
account_words = len(texto.split(' '))
time_seconds = account_words / 2
print('-----------------')
print(f'El tiempo estimado en que tarda en decir esa palabra es de: {time_seconds} segundos')
print(f'Dijo {account_words} palabras.')
print('-----------------')

# B. Si se tarda mas de 1 minuto
# - Decirle: Para flaco tampoco te pedi un testamento
if time_seconds > 60:
    print('Para flaco tampoco te pedi un testamento')
    print('-----------------')

# C. Dalto habla un 30% mas rapido
# - Cuanto tardaria él en decirlo?
time_dalto = time_seconds - ((time_seconds * 30) / 100)
print(f'El tiempo que habla Dalto en esta frase es de: {time_dalto} segundos')