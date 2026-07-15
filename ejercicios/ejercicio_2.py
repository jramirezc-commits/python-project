# Crear una funcion que devuelva los numeros primeros entre el 0 hasta el numero ingresado

def prime_numbers(num):
  is_prime = True
  for number in range(2, num):
    if num % number == 0:
      is_prime = False
      break
  return is_prime

print(prime_numbers(6))


# Crear la serie fibonacci y mostrar sus numeros hasta el numero que reciba la funcion
def show_fibonacci(num):
  fibonacci = []
  step = 0
  while num >= step:
    if len(fibonacci) > 0 and fibonacci[-1] > num:
      # fibonacci.pop()
      del fibonacci[-1]
      break
    if step == 0:
      fibonacci.append(0)
    elif step == 1:
      fibonacci.append(1)
    else:
      fibonacci.append(fibonacci[step - 1] + fibonacci[step - 2])
    step += 1
  return fibonacci


result = show_fibonacci(20)
print('-----------------------------')
print(f'El valor del fibonacci completo es: {result}')