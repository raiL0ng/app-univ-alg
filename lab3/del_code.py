import numpy as np


# Построение объединение бинарных отношений
def get_union_bin_rel(br1, br2=[]):
  if br2 == []:
    union = br1.copy()
    for pair in br1:
      if pair not in union:
        union.append(pair)
    print('Answer:')
    print_binary_relation(union, len(union))
  else:
    union = br1.copy()
    for pair in br2:
      if pair not in union:
        union.append(pair)
    print('Answer:')
    print_binary_relation(union, len(union))


# Построение пересечения бинарных отношений
def get_intersection_bin_rel(br1, br2=[]):
  if br2 == []:
    intersec = []
    for x1, y1 in br1:
      for x2, y2 in br1:
        if x1 == x2 and y1 == y2:
          intersec.append((x1, y1))
    print('Answer:')
    print_binary_relation(intersec, len(intersec))
  else:
    intersec = []
    for x1, y1 in br1:
      for x2, y2 in br2:
        if x1 == x2 and y1 == y2:
          intersec.append((x1, y1))
    print('Answer:')
    print_binary_relation(intersec, len(intersec))


# Построение обратного бинарного отношения
def get_reverse_bin_rel(br):
  rev_br = []
  for x, y in br:
    rev_br.append((y, x))
  print('Answer:')
  print_binary_relation(rev_br, len(rev_br))


# Построение композиции бинарных отношений
def get_composition_bin_rel(br1, br2=[]):
  if br2 == []:
    comp_br = []
    for x1, y1 in br1:
      for x2, y2 in br1:
        if y1 == x2:
          comp_br.append((x1, y2))
    print('Answer:')
    print_binary_relation(comp_br, len(comp_br))
  else:
    comp_br = []
    for x1, y1 in br1:
      for x2, y2 in br2:
        if y1 == x2:
          comp_br.append((x1, y2))
    print('Answer:')
    print_binary_relation(comp_br, len(comp_br))


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
  for i in range(m):
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
  for i in range(len(a)):
    tmp = []
    for j in range(len(a[i])):
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
    print('{ ', end='')
    for i in range(n):
        if i == n - 1:
            print('(' + str(br[i][0]) + ', ' + str(br[i][1]), end=')')
        else:
            print('(' + str(br[i][0]) + ', ' + str(br[i][1]), end='), ')
    print(' }')


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
  is_invertible = True
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      if not (a[i][j] == a[j][i] == '1'):
        is_invertible = False
        break
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
          is_invertible = False
          break
  if is_distributive:
    print('Binary operation is distributive')
  else:
    print('Binary operation is not distributive')


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
def check_all_bin_rel_properties(br1, br2=[]):
  if br2 == []:
    print('Your binary relation:')
    print_binary_relation(br1, len(br1))
    print('Choose operation:')
    print('Press 1 to get union of binary relation')
    print('Press 2 to get intersection of binary relation')
    print('Press 3 to get reverse binary relation')
    print('Press 4 to get composition of binary relation')
    bl = input()
    if bl == '1':
      get_union_bin_rel(br1)
      check_all_bin_rel_properties(br1)
    elif bl == '2':
      get_intersection_bin_rel(br1)
      check_all_bin_rel_properties(br1)
    elif bl == '3':      
      get_reverse_bin_rel(br1)
      check_all_bin_rel_properties(br1)
    elif bl == '4':
      get_composition_bin_rel(br1)
      check_all_bin_rel_properties(br1)
    else:
      return choose_mode()
  else:
    print('Your binary relations:')
    print('First:', end='')
    print_binary_relation(br1, len(br1))
    print('Second', end='')
    print_binary_relation(br2, len(br2))
    print('Choose operation:')
    print('Press 1 to get union of binary relations')
    print('Press 2 to get intersection of binary relations')
    print('Press 3 to get reverse binary relations')
    print('Press 4 to get composition of binary relations')
    bl = input()
    if bl == '1':
      get_union_bin_rel(br1, br2)
      check_all_bin_rel_properties(br1, br2)
    elif bl == '2':
      get_intersection_bin_rel(br1, br2)
      check_all_bin_rel_properties(br1, br2)
    elif bl == '3':
      print('First:', end='')
      get_reverse_bin_rel(br1)
      print('Second', end='')
      get_reverse_bin_rel(br2)
      check_all_bin_rel_properties(br1, br2)
    elif bl == '4':
      get_composition_bin_rel(br1, br2)
      check_all_bin_rel_properties(br1, br2)
    else:
      print('Exit...')
      return choose_mode()


# Построение бинарных отношений
def construction_of_binary_relation():
    print('Enter numbers of binary relation:')
    s = input()
    tmp = [i for i in s.split(' ')]
    if len(tmp) % 2 != 0:
      print('Incorrect input!')
      return choose_mode()
    else:
      br1 = []
      k = 0
      for i in range(1, len(tmp)):
        if i % 2 != 0:
          br1.append((tmp[i - 1], tmp[i]))
          k += 1
      print('Do you want to enter other binary relation? (0 - no, 1 - yes):')
      bl = input()
      print('Enter numbers of binary relation:')
      if bl == '1':
        s = input()
        tmp = [i for i in s.split(' ')]
        if len(tmp) % 2 != 0:
          print('Incorrect input!')
          choose_mode()
        else:
          br2 = []
          k = 0
          for i in range(1, len(tmp)):
            if i % 2 != 0:
              br2.append((tmp[i - 1], tmp[i]))
              k += 1
          check_all_bin_rel_properties(br1, br2)
      elif bl == '0':
        check_all_bin_rel_properties(br1)

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