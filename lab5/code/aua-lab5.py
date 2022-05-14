import numpy as np
import math
from itertools import product


def print_set(s):
    print('{', end=' ')
    k = 1
    n = len(s)
    for el in s:
        if k == n:
            print(el, '}')
        else:
            print(str(el) + ',', end=' ')
        k += 1


# Проверка операции на ассоциативность
def check_associative(set_list, a):
  n = len(set_list)
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if a[i][set_list.index(str(a[j][k]))] != \
          a[set_list.index(str(a[i][j]))][k]:
          return False
  return True


def create_subsemigroup():
    print('Enter set values:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Enter Cayley table values:')
    c_tbl = []
    for i in range(len(set_list)):
      c_tbl.append([j for j in input().split()])     
    print('Enter subset values:')
    s = input()
    subset_list = [i for i in s.split(' ')]
    new_subset = subset_list.copy()
    while True:
        tmp_set = []
        for el1 in set_list:
            for el2 in new_subset:
                tmp_set.append(c_tbl[set_list.index(el2)][set_list.index(el1)])
        subsemigroup = set(new_subset).union(set(tmp_set))
        if (subsemigroup == set(new_subset)):
            break
        else:
            new_subset = list(subsemigroup)
    
    subsemigroup = list(subsemigroup)
    subsemigroup.sort()
    print('Your subsemigroup:', end='')
    print_set(subsemigroup, len(subsemigroup))
    choose_mode()


def create_semigroup_via_set():
    print('Enter semigroup values')
    s = input()
    semigroup = [i for i in s.split(' ')]
    n = len(semigroup)
    print('Enter transformation set values:')
    s = input()
    set_list = [i for i in s.split(' ')]
    m = len(set_list)    
    translation_list = []
    for i in range(m):
        print(f"Enter transformation values '{set_list[i]}' via elements of semigroup: ")
        translation = input().split()
        translation_list.append(translation)    

    combinations = []
    for i in range(1, m + 1):
        comb = list(product(''.join([str(elem) for elem in set_list]), repeat=i))
        combinations += comb
    
    ans = {}
    for comb in combinations:
        correlation_list = []
        for i in semigroup:
            semigroup_elem = i
            for generator in comb:
                if semigroup_elem not in semigroup:
                    semigroup_elem = "*"
                else:
                    semigroup_elem = translation_list[set_list.index(generator)] \
                                                     [semigroup.index(semigroup_elem)]
            correlation_list.append(semigroup_elem)
        ans[comb] = correlation_list

    result = {}
    correlations = {}
    for key, value in ans.items():
        if not any(np.array_equal(value, i) for i in result.values()):
            result[key] = value
        else:
            for k, v in result.items():
                if np.array_equal(v, value):
                    correlations[key] = k

    print("Your presentations: ")
    for key, value in result.items():
        print(key, ":\n", value)

    print("Your corelations: ")
    for key, value in correlations.items():
        print(key, "->", value)

    choose_mode()


def get_right_ideal(x, set_list, c_tbl):
    right_ideal = set()
    indx = set_list.index(x)
    for el in c_tbl[indx]:
        right_ideal = right_ideal.union(el)
    return right_ideal


def get_left_ideal(x, set_list, c_tbl):
  left_ideal = set()
  indx = set_list.index(x)
  for i in range(len(c_tbl)):
    left_ideal = left_ideal.union(c_tbl[i][indx])
  return left_ideal


def create_ideals():
    print('Enter set values:')
    s = input()
    set_list = [i for i in s.split(' ')]
    n = len(set_list)
    print('Enter Cayley table values:')
    c_tbl = []
    for i in range(n):
      c_tbl.append([j for j in input().split()])
    
    if check_associative(set_list, c_tbl) == False:
        print('Cayley table isn\'t associative!')
        return choose_mode()
    
    for el in set_list:
        print('-----------------------------------------')
        print(f'Right ideal ({el}]:', end=' ')
        right_ideal = get_right_ideal(el, set_list, c_tbl)
        tmp_set = list(right_ideal)
        tmp_set.sort()
        print_set(tmp_set)
        print(f'Left ideal [{el}):', end=' ')
        left_ideal = get_left_ideal(el, set_list, c_tbl)
        tmp_set = list(left_ideal)
        tmp_set.sort()
        print_set(tmp_set)
        print(f'Ideal [{el}]:', end=' ')
        tmp_set = list(left_ideal.union(right_ideal))
        tmp_set.sort()
        print_set(tmp_set)
    print('-----------------------------------------')
    
    return choose_mode()


def create_table(set_list, n, presentation):
  a = []
  for i in range(n):
    tmp_a = []
    for j in range(n):
      new_word = set_list[i] + set_list[j]
      while True:
          tmp = str(new_word)
          for key, val in presentation.items():
              if key in new_word:
                  new_word = new_word.replace(key, val)
          if tmp == new_word:
              break
      tmp_a.append(new_word)
    a.append(tmp_a)
  return a


def create_semigroup_via_subset():
    print('Enter elements of set:')
    s = input()
    set_list = [i for i in s.split(' ')]
    print('Number of elements in presentation:') 
    k = int(input())
    presentation = {}
    for i in range(k):
        print(f'Enter element №{i + 1}')
        key = input()
        print(f'Enter equivalent of element №{i + 1}')
        val = input()
        presentation[key] = val
    semigroup = set_list.copy()
    while True:
        new_elements = []
        for el1 in semigroup:
            for el2 in semigroup:
                new_word = el1 + el2
                while True:
                    tmp = str(new_word)
                    for key, val in presentation.items():
                        if key in new_word:
                            new_word = new_word.replace(key, val)
                    if tmp == new_word:
                        break
                new_elements.append(new_word)        
        check_semgr = set(semigroup.copy())
        for el in new_elements:
            if el not in semigroup:
                semigroup.append(el)
        if check_semgr == set(semigroup):
            break
        
    print("Your semigroup:")
    print(semigroup)
    tbl = create_table(semigroup, len(semigroup), presentation)
    print('Cayley table:')
    for line in tbl:
        print(line)
    choose_mode()


# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to create ideals of semigroup')
    print('Press 2 to create Grin\'s relations')
    print('Print 3 to create Grin\'s relations via subset')
    print('Press 4 to exit')
    bl = input()
    if bl == '1':
        create_ideals()
    elif bl == '2':
        print('task 2')
    elif bl == '3':
        create_semigroup_via_subset()
    elif bl == '4':
        return
    else:
        print('Incorrect output')
        return choose_mode()


choose_mode()