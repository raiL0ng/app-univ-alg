import numpy as np

# Построение матрицы по бинарному отношению
def go_to_matrix(br, n):
    n = -1
    for pair in br:
        tmp = max(pair)
        n = max(tmp, n)
    n += 1
    a = []
    for i in range(n):
        a.append([0 for j in range(n)])
    for pair in br:
        a[pair[0]][pair[1]] = 1
    return np.array(a)


# Построение бинарного отношения по матрице
def go_to_set(a, n):
    s = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                s.append((i, j))
    return s


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


#
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
      choose_mode()
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
#
def construction_of_binary_relation():
    print('Enter numbers of binary relation:')
    s = input()
    tmp = [i for i in s.split(' ')]
    if len(tmp) % 2 != 0:
      print('Incorrect input!')
      choose_mode()
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


# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to check properties')
    print('Press 2 to execute operations for binary relations')
    print('Press 3 to execute operations for matrix')
    print('Press 4 to exit')
    bl = input()
    if bl == '1':
        print('chmod1')
    elif bl == '2':
        construction_of_binary_relation()
    elif bl == '3':
        print('chmod3')
        a = []
        print('Enter the number of verticies')
        n = int(input())
        print('Enter the matrix values')
        for i in range(n):
          tmp = input().split()
          for j in range(len(tmp)):
                tmp[j] = int(tmp[j])
          a.append(tmp)
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()


choose_mode()