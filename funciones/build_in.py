datos = [5, 1, 7, 10, 3, 8, 12.56]

valor_mas_alto = max(datos)
print(f'valor_mas_alto: {valor_mas_alto}')

valor_mas_bajo = min(datos)
print(f'valor mas bajo: {valor_mas_bajo}')


# Redondea al entero más cercano por defecto (no siempre hacia abajo). Si se le pasa como segundo parametro, se puede controlar cuantos decimales mostrar
redondear_valor = round(datos[len(datos)-1])
print(f'redondear_valor: {redondear_valor}')
redondear_valor_decimales = round(datos[len(datos)-1], 2)
print(f'redondear_valor_decimales: {redondear_valor_decimales}')


# Retorna un false cuando se le pasa: 0, false, None, un valor vacio.
resultado_bool = bool(redondear_valor)
print(f'resultado_bool: {resultado_bool}')

# Retorna un True cuando el dato que se le pasa es iterable y todos sus valores internos son verdaderos (truthy)
# resultado_bool = all(dato is not None for dato in datos) #Valida si los items internos de "datos" no son None
# resultado_bool = all(datos)
resultado_bool = all(['', 1, 'cualquier cosa'])#False, por el primer elemento vacio
print(f'resultado_bool: {resultado_bool}')
