def crear_password_random(num):
  chars = 'iuqhweffdsañlkj'
  num_entero = str(num)
  new_num = int(num_entero[0])
  c1 = chars[new_num + 1]
  c2 = chars[new_num + 5]
  c3 = chars[new_num]
  new_hash = f'{c1 + c2 + c3 + str(new_num * 2)}'
  return new_hash, num