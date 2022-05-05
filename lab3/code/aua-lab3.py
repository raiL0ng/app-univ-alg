import numpy as np


# Проверка операции на идемпотентность
def check_idempotence(set_list, a):
  is_idempotent = True
  for i in range(len(set_list)):
    if a[i][i] != set_list[i]:
      is_idempotent = False
      break
  if is_idempotent:
    print('Binary operation is idempotent')
  else:
    print('Binary operation is not idempotent')


# Проверка операции на коммутативность
def check_commutative(set_list, a):
  is_commutative = True
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      if a[i][j] != a[j][i]:
        is_commutative = False
        break
  if is_commutative:
    print('Binary operation is commutative')
  else:
    print('Binary operation is not commutative')


# Проверка операции на ассоциативность
def check_associative(set_list, a):
  is_associative = True
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if a[i][set_list.index(str(a[j][k]))] != \
          a[set_list.index(str(a[i][j]))][k]:
          is_associative = False
          break
  if is_associative:
    print('Binary operation is associative')
  else:
    print('Binary operation is not associative')


# Проверка операции на обратимость
def check_invertibility(set_list, a):
  is_invertible = False
  n = len(set_list)
  for i in range(n):
    cnt1 = 0
    cnt2 = 0
    for j in range(n):
      if a[i][j] == '1':
        cnt1 += 1
      if a[j][i] == '1':
        cnt2 += 1
    if cnt1 == cnt2 == n:
      is_invertible = True
  if is_invertible:
    print('Binary operation is invertible')
  else:
    print('Binary operation is not invertible')


# Проверка операции на дистрибутивность
def check_distributivity(set_list, a):
  print('Enter matrix values')
  b = []
  for i in range(len(set_list)):
    b.append([j for j in input().split()])

  is_distributive = True
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if (a[i][set_list.index(b[j][k])] != \
           b[set_list.index(a[i][j])][set_list.index(a[i][k])]) \
           or (a[set_list.index(b[j][k])][i] != \
           b[set_list.index(a[j][i])][set_list.index(a[k][i])]):
          is_distributive = False
          break
  if is_distributive:
    print('Binary operation is distributive')
  else:
    print('Binary operation is not distributive')


# Построение объединение бинарных отношений
def get_union_bin_rel(a, b, n):
  c = []
  for i in range(n):
    tmp = []
    for j in range(len(a[i])):
      if a[i][j] and b[i][j]:
        tmp.append(1)
      else:
        tmp.append(a[i][j] + b[i][j])
    c.append(tmp)
  print('*******************************************')
  print_matrix(c, n)
  go_to_set(c, n)
  print('*******************************************')


# Построение пересечения бинарных отношений
def get_intersection_bin_rel(a, b, n):
  c = []
  for i in range(n):
    tmp = []
    for j in range(len(a[i])):
      tmp.append(a[i][j] * b[i][j])
    c.append(tmp)
  print('*******************************************')
  print_matrix(c, n)
  go_to_set(c, n)
  print('*******************************************')


# Построение дополнения бинарного отношения
def get_addition_bin_rel(a, n):
  c = []
  for i in range(n):
    tmp = []
    for j in range(n):
      tmp.append(1 - a[i][j])
    c.append(tmp)
  print('*******************************************')
  print_matrix(c, n)
  go_to_set(c, n)
  print('*******************************************')


# Построение обратного бинарного отношения
def get_reverse_bin_rel(a, n):
  c = np.array(a)
  c = c.transpose()
  print('*******************************************')
  print_matrix(c, n)
  go_to_set(c, n)
  print('*******************************************')


# Построение композиции бинарных отношений
def get_composition_bin_rel(a, b, n):
  c = []
  for i in range(n):
    tmp = []
    for j in range(n):
      sum = 0
      for k in range(n):
        sum += a[i][k] * b[k][j]
        if sum > 1:
          sum = 1
      tmp.append(sum)
    c.append(tmp)
  print('*******************************************')
  print_matrix(c, n)
  go_to_set(c, n)
  print('*******************************************')

# Выполнение операции сложения матриц
def get_addition_operation(a, n):
  print('Enter values of another matrix')
  b = []
  for i in range(n):
    tmp = input().split()
    for j in range(len(tmp)):
      try:
        tmp[j] = float(tmp[j])
      except:
        k = 0
      else:
        tmp[j] = float(tmp[j])
    b.append(tmp)
  c = []
  for i in range(n):
    tmp = []
    for j in range(len(a[i])):
      tmp.append(a[i][j] + b[i][j])
    c.append(tmp)
  return c


# Выполнение операции вычитания матриц
def get_subtraction_operation(a, n):
  print('Enter values of another matrix')
  b = []
  for i in range(n):
    tmp = input().split()
    for j in range(len(tmp)):
      try:
        tmp[j] = float(tmp[j])
      except:
        k = 0
      else:
        tmp[j] = float(tmp[j])
    b.append(tmp)
  c = []
  for i in range(n):
    tmp = []
    for j in range(len(a[i])):
      tmp.append(a[i][j] - b[i][j])
    c.append(tmp)
  return c


# Выполнение операции умножение матрицы на число
def get_multiplication_matrix_on_number(a):
  print('Enter number:')
  num = float(input())
  c = []
  for i in range(len(a)):
    tmp = []
    for j in range(len(a[i])):
      tmp.append(a[i][j] * num)
    c.append(tmp)
  return c


# Выполнение операции умножения матриц
def get_multiplication_operation(a):
  print('Enter the number of rows')
  n = int(input())
  print('Enter the number of columns')
  m = int(input())
  print('Enter values of another matrix')
  b = []
  for i in range(n):
    tmp = input().split()
    for j in range(m):
      try:
        tmp[j] = float(tmp[j])
      except:
        k = 0
      else:
        tmp[j] = float(tmp[j])
    b.append(tmp)
  c = []
  for i in range(len(a)):
    tmp = []
    for j in range(m):
      sum = 0
      for k in range(n):
        sum += a[i][k] * b[k][j]
      tmp.append(sum)
    c.append(tmp)
  return c


# Выполнение операции транспонирования матрицы
def get_transpose_operation(a):
  c = []
  n = len(a)
  m = len(a[0])
  for i in range(m):
    tmp = []
    for j in range(n):
      tmp.append(a[j][i])
    c.append(tmp)
  return c


# Нахождение обратной матрицы
def get_inverse_matrix(a):
  a = np.array(a)
  return np.linalg.inv(a)


# Вывод матрицы
def print_matrix(a, n):
    cnt = 0
    print('Your matrix:')
    for i in a:
        if (cnt < n):
            print(f'{i}' + ' ')
        else:
            print(f'{i}' + '\n')
            cnt = 0
        cnt += 1


# Вывод бинарного отношения
def print_binary_relation(br, n):
    print('Your binary relation')
    print('{ ', end='')
    for i in range(n):
        if i == n - 1:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end=')')
        else:
            print('(' + str(br[i][0] + 1) + ', ' + str(br[i][1] + 1), end='), ')
    print(' }')


# Построение бинарного отношения по матрице
def go_to_set(a, n):
    s = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                s.append((i, j))

    print_binary_relation(s, len(s))


# Проверка свойств (меню)
def check_properties_mode(set_list, a):
    print_matrix(a, len(a))
    print('Press 1 to check idempotence property')
    print('Press 2 to check commutative property')
    print('Press 3 to check associative property')
    print('Press 4 to check invertibility property')
    print('Press 5 to check distributivity property')
    print('Press 6 to exit')
    bl = input()
    if bl == '1':
      check_idempotence(set_list, a)
      check_properties_mode(set_list, a)
    elif bl == '2':
      check_commutative(set_list, a)
      check_properties_mode(set_list, a)
    elif bl == '3':
      check_associative(set_list, a)
      check_properties_mode(set_list, a)
    elif bl == '4':
      check_invertibility(set_list, a)
      check_properties_mode(set_list, a)
    elif bl == '5':
      check_distributivity(set_list, a)
      check_properties_mode(set_list, a)
    else:
      return choose_mode()


# Проверка свойств бинарных отношений
def check_all_bin_rel_properties(a, b=[]):
  if b == []:
    print_matrix(a, len(a))
    go_to_set(a, len(a))
    print('Choose operation:')
    print('Press 1 to get union of binary relation')
    print('Press 2 to get intersection of binary relation')
    print('Press 3 to get addition binary relation')
    print('Press 4 to get reverse binary relation')
    print('Press 5 to get composition of binary relation')
    bl = input()
    if bl == '1':
      get_union_bin_rel(a, a, len(a))
      check_all_bin_rel_properties(a)
    elif bl == '2':
      get_intersection_bin_rel(a, a, len(a))
      check_all_bin_rel_properties(a)
    elif bl == '3':      
      get_addition_bin_rel(a, len(a))
      check_all_bin_rel_properties(a)
    elif bl == '4':      
      get_reverse_bin_rel(a, len(a))
      check_all_bin_rel_properties(a)
    elif bl == '5':
      get_composition_bin_rel(a, a, len(a))
      check_all_bin_rel_properties(a)
    else:
      print('Exit...')
  else:
    print('Your binary relations matrix:')
    print('First:')
    print_matrix(a, len(a))
    go_to_set(a, len(a))
    print('Second:')
    print_matrix(b, len(b))
    go_to_set(b, len(b))
    print('Choose operation:')
    print('Press 1 to get union of binary relations')
    print('Press 2 to get intersection of binary relations')
    print('Press 3 to get addition binary relations')
    print('Press 4 to get reverse binary relations')
    print('Press 5 to get composition of binary relations')
    bl = input()
    if bl == '1':
      get_union_bin_rel(a, b, len(a))
      check_all_bin_rel_properties(a, b)
    elif bl == '2':
      get_intersection_bin_rel(a, b, len(a))
      check_all_bin_rel_properties(a, b)
    elif bl == '3':
      print('First:', end='')
      get_addition_bin_rel(a, len(a))
      print('Second:', end='')
      get_addition_bin_rel(b, len(b))
      check_all_bin_rel_properties(a, b)
    elif bl == '4':
      print('First:', end='')
      get_reverse_bin_rel(a, len(a))
      print('Second:', end='')
      get_reverse_bin_rel(b, len(b))
      check_all_bin_rel_properties(a, b)
    elif bl == '5':
      get_composition_bin_rel(a, b, len(a))
      check_all_bin_rel_properties(a, b)
    else:
      print('Exit...')


# Построение бинарных отношений
def construction_of_binary_relation():
    print('Enter number of binary relation elements')
    n = int(input())
    print('Enter values of binary relation matrix')
    a = []
    for i in range(n):
      tmp = input().split()
      for j in range(len(tmp)):
        tmp[j] = int(tmp[j])
      a.append(tmp)
    print('Do you want to enter other binary relation? (0 - no, 1 - yes):')
    bl = input()
    if bl == '1':
      print('Enter values of binary relation matrix')
      b = []
      for i in range(n):
        tmp = input().split()
        for j in range(len(tmp)):
          tmp[j] = int(tmp[j])
        b.append(tmp)
      check_all_bin_rel_properties(a, b)
    elif bl == '0':
      check_all_bin_rel_properties(a)

    return choose_mode()


# Построение матриц
def construction_of_matrix(a):
  print_matrix(a, len(a))
  n = len(a)
  print('Choose operation:')
  print('Press 1 to add another matrix')
  print('Press 2 to subtract another matrix')
  print('Press 3 to multiply this matrix on number')
  print('Press 4 to multiply on another matrix')
  print('Press 5 to transpose this matrix')
  print('Press 6 to find inverse matrix')
  bl = input()
  if bl == '1':
    a = get_addition_operation(a, n)
    construction_of_matrix(a)
  elif bl == '2':
    a = get_subtraction_operation(a, n)
    construction_of_matrix(a)
  elif bl == '3':
    a = get_multiplication_matrix_on_number(a)
    construction_of_matrix(a)
  elif bl == '4':
    a = get_multiplication_operation(a)
    construction_of_matrix(a)
  elif bl == '5':
    a = get_transpose_operation(a)
    construction_of_matrix(a)
  elif bl == '6':
    a = get_inverse_matrix(a)
    construction_of_matrix(a)
  else:
    return choose_mode()


# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to check properties')
    print('Press 2 to execute operations for binary relations')
    print('Press 3 to execute operations for matrix')
    print('Press 4 to exit')
    bl = input()
    if bl == '1':
        print('Enter numbers of set:')
        s = input()
        set_list = [i for i in s.split(' ')]
        print('Enter matrix values')
        a = []
        for i in range(len(set_list)):
          a.append([j for j in input().split()])
        check_properties_mode(set_list, a)
    elif bl == '2':
        construction_of_binary_relation()
    elif bl == '3':
        a = []
        print('Enter the number of rows')
        n = int(input())
        print('Enter the number of columns')
        m = int(input())
        print('Enter the matrix values')
        for i in range(n):
          tmp = input().split()
          for j in range(m):
              try:
                tmp[j] = float(tmp[j])
              except:
                k = 0
              else:
                tmp[j] = float(tmp[j])
          a.append(tmp)
        construction_of_matrix(a)
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()


choose_mode()