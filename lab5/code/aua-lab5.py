import numpy as np


# Вывод множества
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


# Построение правых идеалов
def get_right_ideal(x, set_list, c_tbl):
    right_ideal = set()
    indx = set_list.index(x)
    for el in c_tbl[indx]:
        right_ideal.add(el)
    return right_ideal


# Построение левых идеалов
def get_left_ideal(x, set_list, c_tbl):
  left_ideal = set()
  indx = set_list.index(x)
  for i in range(len(c_tbl)):
    left_ideal.add(c_tbl[i][indx])
  return left_ideal


# Обход в глубину (топологическая сортировка)
def dfs(gr, visited, v, order):
    visited[v] = True
    for i in range(len(gr)):
        u = i
        if (not(visited[u]) and gr[v][u]):
            dfs(gr, visited, u, order)
    order.append(v)


# Обход в глубину
def dfs1(t_gr, visited, v, component):
    visited[v] = True
    component.append(v)
    for i in range(len(t_gr)):
        u = i
        if (not(visited[u]) and t_gr[v][u]):
            dfs1(t_gr, visited, u, component)


# Вывод egg-box-картины
def print_egg_boxes(semigroup, egg_box):
    print('Your egg-box-diagram:')
    print('{* 1 }')
    for box in egg_box:
        print('{*', end=' ')
        for i in range(len(box)):
            print(semigroup[box[i]], end=' ')
        print('}')


# Построение egg-box-картины 
def get_egg_boxes(semigroup, d):
    n = len(d)
    order = []
    component = []
    visited = [False for _ in range(n)]
    for i in range(n):
        if (not(visited[i])):
            dfs(d, visited, i, order)
    visited = [False for _ in range(n)]
    egg_box = []
    for i in range(n):
        v = order[n - 1 - i]
        if (not(visited[v])):
            dfs1(d.T, visited, v, component)
            egg_box.append(component.copy())
            component.clear()
    order.clear()
    return egg_box


# Построение отношеня Грина
def create_Grin_relation(semigroup, right_ideals_dict, left_ideals_dict):
    r = []
    l = []
    for el1 in semigroup:
        tmp_a = []
        tmp_b = []
        for el2 in semigroup:
            if right_ideals_dict[el1] == right_ideals_dict[el2]:
                tmp_a.append(1)
            else:
                tmp_a.append(0)
            if left_ideals_dict[el1] == left_ideals_dict[el2]:
                tmp_b.append(1)
            else:
                tmp_b.append(0)
        r.append(tmp_a)
        l.append(tmp_b)
    n = len(semigroup)
    d = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if r[i][j] == l[i][j] == 1:
                d[i][j] = 1
            else:
                d[i][j] = r[i][j] + l[i][j]
            
    print('Your Grin\'s relation:')
    for el in d:
        print(el)
    
    print('Would you like to get egg-box-diagram? (1 - "yes")')
    bl = input()
    if bl == '1':
        egg_box_list = get_egg_boxes(semigroup, d)

    print_egg_boxes(semigroup, egg_box_list)


# Построение идеалов относительно каждого элемента
def get_and_set_ideals(semigroup, c_tbl):
    right_ideals_dict = {}
    left_ideals_dict = {}
    for el in semigroup:
        print('-----------------------------------------')
        print(f'Right ideal ({el}]:', end=' ')
        right_ideals_dict[el] = get_right_ideal(el, semigroup, c_tbl)
        tmp_set = list(right_ideals_dict[el])
        tmp_set.sort()
        print_set(tmp_set)
        print(f'Left ideal [{el}):', end=' ')
        left_ideals_dict[el] = get_left_ideal(el, semigroup, c_tbl)
        tmp_set = list(left_ideals_dict[el])
        tmp_set.sort()
        print_set(tmp_set)
        print(f'Ideal [{el}]:', end=' ')
        tmp_set = list(left_ideals_dict[el].union(right_ideals_dict[el]))
        tmp_set.sort()
        print_set(tmp_set)
    print('-----------------------------------------')
    return right_ideals_dict, left_ideals_dict


# Построение идеалов (меню)
def create_ideals():
    print('Enter set values:')
    s = input()
    semigroup = [i for i in s.split(' ')]
    n = len(semigroup)
    print('Enter Cayley table values:')
    c_tbl = []
    for i in range(n):
      c_tbl.append([j for j in input().split()])
    
    if check_associative(semigroup, c_tbl) == False:
        print('Cayley table isn\'t associative!')
        return choose_mode()
    
    right_ideals_dict, left_ideals_dict = get_and_set_ideals(semigroup, c_tbl)
    
    print('Would you to create Grin\'s relation? (1 - "yes")')
    bl = input()
    if bl == '1':
        create_Grin_relation(semigroup, right_ideals_dict, left_ideals_dict)
    return choose_mode()


# Построение таблицы Кэли по полугруппе
def create_table(semigroup, n, presentation):
    a = []
    for i in range(n):
        tmp_a = []
        for j in range(n):
            new_word = semigroup[i] + semigroup[j]
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


# Построение полугруппы по копредставлению
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
                    tmp = new_word
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
    
    if check_associative(semigroup, tbl) == False:
        print('Cayley table isn\'t associative!')
        return choose_mode()
    
    right_ideals_dict, left_ideals_dict = get_and_set_ideals(semigroup, tbl)
    
    print('Would you to create Grin\'s relation? (1 - "yes")')
    bl = input()
    if bl == '1':
        create_Grin_relation(semigroup, right_ideals_dict, left_ideals_dict)
    
    choose_mode()


# Главное меню
def choose_mode():
    print('Choose mode:')
    print('Press 1 to create Grin\'s relations')
    print('Press 2 to create Grin\'s relations via subset')
    print('Press 3 to exit')
    bl = input()
    if bl == '1':
        create_ideals()
    elif bl == '2':
        create_semigroup_via_subset()
    elif bl == '3':
        return
    else:
        print('Incorrect output')
        return choose_mode()


if __name__ == "__main__":
    choose_mode()